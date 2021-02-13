from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Person, BoardGame, Furniture, ETC, OPTION_DICT
from django.contrib import messages
import random

access_id = "20210311" 

def get_lot_winner():
	winner_list = []
	for book in Book.objects.all():
		people_num = book.people.count()
		people_list = list(book.people.all())
		book_num = book.quantity
		if people_num == 0:
			pass
		elif people_num <= book_num:
			for i in range(people_num):
				winner_list.append([people_list[i], book])
		else:
			lot_list = random.sample(people_list, book_num)
			for person in lot_list:
				winner_list.append([person, book])
	for board_game in BoardGame.objects.all():
		people_num = board_game.people.count()
		people_list = list(board_game.people.all())
		board_game_num = board_game.quantity
		if people_num == 0:
			pass
		elif people_num <= board_game_num:
			for i in range(people_num):
				winner_list.append([people_list[i], board_game])
		else:
			lot_list = random.sample(people_list, board_game_num)
			for person in lot_list:
				winner_list.append([person, board_game])

	for furniture in Furniture.objects.all():
		people_num = furniture.people.count()
		people_list = list(furniture.people.all())
		furniture_num = furniture.quantity
		if people_num == 0:
			pass
		elif people_num <= furniture_num:
			for i in range(people_num):
				winner_list.append([people_list[i], furniture])
		else:
			lot_list = random.sample(people_list, furniture_num)
			for person in lot_list:
				winner_list.append([person, furniture])

	for etc in ETC.objects.all():
		people_num = etc.people.count()
		people_list = list(etc.people.all())
		etc_num = etc.quantity
		if people_num == 0:
			pass
		elif people_num <= etc_num:
			for i in range(people_num):
				winner_list.append([people_list[i], etc])
		else:
			lot_list = random.sample(people_list, etc_num)
			for person in lot_list:
				winner_list.append([person, etc])

	return winner_list


def lot(request):
	if request.method == "POST":
		access_id_get = str(request.POST.get("access_id"))
		if access_id_get == access_id:
			winner_list = get_lot_winner()
			return render(request, 'lotWinner.html', {
										 'winner_list':winner_list,
										})

		else:
			messages.error(request, '접근번호가 틀렸습니다.')
			return render(request, 'lot.html')

	else:
		return render(request, 'lot.html')

def get_status():
	status_list = []
	for obj in Book.objects.all():
		people_num = obj.people.count()
		people_list = list(obj.people.all())
		for i in range(people_num):
			status_list.append([people_list[i], obj])

	for obj in BoardGame.objects.all():
		people_num = obj.people.count()
		people_list = list(obj.people.all())
		for i in range(people_num):
			status_list.append([people_list[i], obj])

	for obj in Furniture.objects.all():
		people_num = obj.people.count()
		people_list = list(obj.people.all())
		for i in range(people_num):
			status_list.append([people_list[i], obj])

	for obj in ETC.objects.all():
		people_num = obj.people.count()
		people_list = list(obj.people.all())
		for i in range(people_num):
			status_list.append([people_list[i], obj])


	return status_list


def status(request):
	if request.method == "POST":
		access_id_get = str(request.POST.get("access_id"))
		if access_id_get == access_id:
			status_list = get_status()
			return render(request, 'statusResult.html', {
										 'status_list':status_list,
										})

		else:
			messages.error(request, '접근번호가 틀렸습니다.')
			return render(request, 'status.html')

	else:
		return render(request, 'status.html')

def home(request):
	price_sum = 0
	for book in Book.objects.all(): price_sum += book.price * book.quantity
	for board_game in BoardGame.objects.all(): price_sum += board_game.price * board_game.quantity
	for furniture in Furniture.objects.all(): price_sum += furniture.price * furniture.quantity
	for etc in ETC.objects.all(): price_sum += etc.price * etc.quantity
	people_num = Person.objects.all().count()
	return render(request, 'home.html', {
										 'people_num':people_num,
										 'price_sum':price_sum,
										})

def signup(request):
	person_list = Person.objects.all()
	if request.method == "POST":
		_name = request.POST.get("name")
		_student_id = request.POST.get("student_id")
		_major = request.POST.get("major")
		_password = request.POST.get("password")
		_password_check = request.POST.get("password_check")

		if (_password != _password_check):
			messages.error(request, '비밀번호가 일치하지 않습니다.')
			return render(request, 'signUp.html')

		else:
			if len(_student_id) != 9:
				messages.error(request, '학번은 9자리로 입력해야 합니다.')
				return render(request, 'signUp.html')
			elif not _student_id.isdigit():
				messages.error(request, '학번에는 숫자만 입력하야 합니다.')
				return render(request, 'signUp.html')
			for person in person_list:
				if (person.student_id == _student_id):
					messages.error(request, '이미 가입하셨습니다.')
					return render(request, 'signUp.html')
			_person = Person()
			_person.name = _name
			_person.student_id = _student_id
			_person.major = _major
			_person.password = _password
			_person.save()
			return redirect("/")


	else:
		return render(request, 'signUp.html')


def book_list(request):
	book_list = Book.objects.all()
	return render(request, 'bookList.html', {
										 'book_list':book_list,
										 'option_dict':OPTION_DICT,
										})


def book(request, book_id):
	book = Book.objects.get(id=book_id)
	people_num = book.people.all().count()
	return render(request, 'book.html', {
										 'book' : book,
										 'people_num' : people_num,
										})

def register_book(request, book_id = 0):
	if request.method == "POST":
		book = Book.objects.get(id=int(request.POST.get("book_id")))
		people = book.people.all()
		_student_id = request.POST.get("student_id")
		_password = request.POST.get("password")
		for person in people:
			if (person.student_id == _student_id and person.password == _password):
				messages.error(request, '이미 대기열에 등록하셨습니다.')
				return redirect('registerBook/' + request.POST.get("book_id"))
		
		person = Person.objects.filter(student_id = request.POST["student_id"])
		if len(person) and person[0].password == _password:
			book.people.add(person[0])
		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('registerBook/' + request.POST.get("book_id"))

		return redirect('book/' + request.POST.get("book_id"))

	else:
		book = Book.objects.get(id=book_id)
		return render(request, 'registerBook.html', {
										 'book' : book,
										})


def unRegister_book(request, book_id = 0):
	if request.method == "POST":
		book = Book.objects.get(id=int(request.POST.get("book_id")))
		people = book.people.all()
		person = Person.objects.filter(student_id = request.POST["student_id"])
		_password = request.POST["password"]
		if len(person):
			if person[0].password == _password:
				for p in people:
					if p.id == person[0].id:
						book.people.remove(person[0])
						return redirect('book/' + request.POST.get("book_id"))
				messages.error(request, '이미 대기열을 취소하셨거나, 대기열을 등록하신 적이 없습니다.')
				return redirect('unRegisterBook/' + request.POST.get("book_id"))
			else:
				messages.error(request, '비밀번호가 올바르지 않습니다.')
				return redirect('unRegisterBook/' + request.POST.get("book_id"))

		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('unRegisterBook/' + request.POST.get("book_id"))

	else:
		book = Book.objects.get(id=book_id)
		return render(request, 'unRegisterBook.html', {
										 'book' : book,
										})
def board_game_list(request):
	board_game_list = BoardGame.objects.all()
	return render(request, 'boardGameList.html', {
										 'board_game_list':board_game_list,
										})


def board_game(request, board_game_id):
	board_game = BoardGame.objects.get(id=board_game_id)
	people_num = board_game.people.all().count()
	return render(request, 'boardGame.html', {
										 'board_game' : board_game,
										 'people_num' : people_num,
										})


def register_board_game(request, board_game_id = 0):
	if request.method == "POST":
		board_game = BoardGame.objects.get(id=int(request.POST.get("board_game_id")))
		people = board_game.people.all()
		_student_id = request.POST.get("student_id")
		_password = request.POST.get("password")
		for person in people:
			if (person.student_id == _student_id and person.password == _password):
				messages.error(request, '이미 대기열에 등록하셨습니다.')
				return redirect('registerBoardGame/' + request.POST.get("board_game_id"))

		person = Person.objects.filter(student_id = request.POST["student_id"])
		if len(person) and person[0].password == _password:
			board_game.people.add(person[0])
		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('registerBoardGame/' + request.POST.get("board_game_id"))

		return redirect('boardGame/' + request.POST.get("board_game_id"))

	else:
		board_game = BoardGame.objects.get(id=board_game_id)
		return render(request, 'registerBoardGame.html', {
										 'board_game' : board_game,
										})

def unRegister_board_game(request, board_game_id = 0):
	if request.method == "POST":
		board_game = BoardGame.objects.get(id=int(request.POST.get("board_game_id")))
		people = board_game.people.all()
		person = Person.objects.filter(student_id = request.POST["student_id"])
		_password = request.POST["password"]
		if len(person):
			if person[0].password == _password:
				for p in people:
					if p.id == person[0].id:
						board_game.people.remove(person[0])
						return redirect('boardGame/' + request.POST.get("board_game_id"))
				messages.error(request, '이미 대기열을 취소하셨거나, 대기열을 등록하신 적이 없습니다.')
				return redirect('unRegisterBoardGame/' + request.POST.get("board_game_id"))

			else:
				messages.error(request, '비밀번호가 올바르지 않습니다.')
				return redirect('unRegisterBoardGame/' + request.POST.get("board_game_id"))

		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('unRegisterBoardGame/' + request.POST.get("board_game_id"))

	else:
		board_game = BoardGame.objects.get(id=board_game_id)
		return render(request, 'unRegisterBoardGame.html', {
										 'board_game' : board_game,
										})

def furniture_list(request):
	furniture_list = Furniture.objects.all()
	return render(request, 'furnitureList.html', {
										 'furniture_list':furniture_list,
										})


def furniture(request, furniture_id):
	furniture = Furniture.objects.get(id=furniture_id)
	people_num = furniture.people.all().count()
	return render(request, 'furniture.html', {
										 'furniture' : furniture,
										 'people_num' : people_num,
										})


def register_furniture(request, furniture_id = 0):
	if request.method == "POST":
		furniture = Furniture.objects.get(id=int(request.POST.get("furniture_id")))
		people = furniture.people.all()
		_student_id = request.POST.get("student_id")
		_password = request.POST.get("password")

		for person in people:
			if (person.student_id == _student_id and person.password == _password):
				messages.error(request, '이미 대기열에 등록하셨습니다.')
				return redirect('registerFurniture/' + request.POST.get("furniture_id"))

		person = Person.objects.filter(student_id = request.POST.get("student_id"))
		if len(person) and person[0].password == _password:
			furniture.people.add(person[0])
		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('registerFurniture/' + request.POST.get("furniture_id"))

		return redirect('furniture/' + request.POST.get("furniture_id"))

	else:
		furniture = Furniture.objects.get(id=furniture_id)
		return render(request, 'registerFurniture.html', {
										 'furniture' : furniture,
										})

def unRegister_furniture(request, furniture_id = 0):
	if request.method == "POST":
		furniture = Furniture.objects.get(id=int(request.POST.get("furniture_id")))
		people = furniture.people.all()
		person = Person.objects.filter(student_id = request.POST["student_id"])
		_password = request.POST["password"]

		if len(person):
			if person[0].password == _password:
				for p in people:
					if p.id == person[0].id:
						furniture.people.remove(person[0])
						return redirect('furniture/' + request.POST.get("furniture_id"))

				messages.error(request, '이미 대기열을 취소하셨거나, 대기열을 등록하신 적이 없습니다.')
				return redirect('unRegisterFurniture/' + request.POST.get("furniture_id"))

			else:
				messages.error(request, '비밀번호가 올바르지 않습니다.')
				return redirect('unRegisterFurniture/' + request.POST.get("furniture_id"))

		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('unRegisterFurniture/' + request.POST.get("furniture_id"))

	else:
		furniture = Furniture.objects.get(id=furniture_id)
		return render(request, 'unRegisterFurniture.html', {
										 'furniture' : furniture,
										})

def etc_list(request):
	etc_list = ETC.objects.all()
	return render(request, 'etcList.html', {
										 'etc_list':etc_list,
										})


def etc(request, etc_id):
	etc = ETC.objects.get(id=etc_id)
	people_num = etc.people.all().count()
	return render(request, 'etc.html', {
										 'etc' : etc,
										 'people_num' : people_num,
										})

def register_etc(request, etc_id = 0):
	if request.method == "POST":
		etc = ETC.objects.get(id=int(request.POST.get("etc_id")))
		people = etc.people.all()
		_student_id = request.POST.get("student_id")
		_password = request.POST.get("password")

		for person in people:
			if (person.student_id == _student_id and person.password == _password):
				messages.error(request, '이미 대기열에 등록하셨습니다.')
				return redirect('registerETC/' + request.POST.get("etc_id"))
		
		person = Person.objects.filter(student_id = request.POST["student_id"])
		if len(person) and person[0].password == _password:
			etc.people.add(person[0])
		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('registerETC/' + request.POST.get("etc_id"))

		return redirect('etc/' + request.POST.get("etc_id"))

	else:
		etc = ETC.objects.get(id=etc_id)
		return render(request, 'registerETC.html', {
										 'etc' : etc,
										})


def unRegister_etc(request, etc_id = 0):
	if request.method == "POST":
		etc = ETC.objects.get(id=int(request.POST.get("etc_id")))
		people = etc.people.all()
		person = Person.objects.filter(student_id = request.POST["student_id"])
		_password = request.POST["password"]

		if len(person):
			if person[0].password == _password:
				for p in people:
					if p.id == person[0].id:
						etc.people.remove(person[0])
						return redirect('etc/' + request.POST.get("etc_id"))

				messages.error(request, '이미 대기열을 취소하셨거나, 대기열을 등록하신 적이 없습니다.')
				return redirect('unRegisterETC/' + request.POST.get("etc_id"))
			else:
				messages.error(request, '비밀번호가 올바르지 않습니다.')
				return redirect('unRegisterETC/' + request.POST.get("etc_id"))

		else:
			messages.error(request, '학번 또는 비밀번호가 올바르지 않습니다.')
			return redirect('unRegisterETC/' + request.POST.get("etc_id"))

	else:
		etc = ETC.objects.get(id=etc_id)
		return render(request, 'unRegisterETC.html', {
										 'etc' : etc,
										})











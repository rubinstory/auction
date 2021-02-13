from django.db import models
import os

OPTION_DICT = {
			"Freshmen":"1학년",
			"Computer":"컴공",
			"Electrical":"전기",
			"Electric":"전자",
			"Elective":"교양",
			"ETC":"기타"
		}

MAJOR_DICT = {
			"CSE":"정보컴퓨터공학과",
			"EEC":"전기공학과",
			"EE":"전자공학과",
			"ETC":"기타"
		}

class Person(models.Model):
	name = models.CharField(
			default = "",
			max_length = 100,
			help_text = "이름을 입력하세요"
		)
	major = models.CharField(
			default = "기타",
			max_length = 100,
			help_text = "전공을 입력하세요"
		)
	student_id = models.CharField(
			default = "",
			max_length = 100,
			help_text = "학번을 입력하세요"
		)

	password = models.CharField(
			default = "password",
			max_length = 100,
			help_text = "비밀번호를 입력하세요"
		)

	def __str__(self):
		return self.name + "(" + self.major + ", " + self.student_id + ")"


class Book(models.Model):
	OPTION_LIST = (
			("Freshmen", "1학년"),
			("Computer", "컴공"),
			("Electrical", "전기"),
			("Electric", "전자"),
			("Elective", "교양"),
			("ETC", "기타"),
		)
	name = models.CharField(
			default = "",
			max_length = 100,
			help_text = "책 이름을 입력하세요"
		)

	quantity = models.IntegerField(
			default = 1,
			help_text = "수량"
		)

	origin_price = models.IntegerField(
			default = 0,
			help_text = "원래 금액 / 모르면 0원"
		)

	price = models.IntegerField(
			default = 0,
			help_text = "판매 금액"
		)
	category = models.CharField(
			choices = OPTION_LIST,
			default = OPTION_LIST[-1][0],
			max_length = 100,
			help_text = "책의 종류를 선택하세요"
		)

	image = models.ImageField(
			upload_to = 'images/books', 
			blank = True, 
			null = True,
			help_text='책의 이미지를 업로드하세요'
		)

	people = models.ManyToManyField(
			Person,
			blank = True,
			help_text = '해당 책을 선택한 사람들의 목록입니다.'
		)


	def __str__(self):
		return self.name

	def getCategory(self):
		return OPTION_DICT[self.category]

class BoardGame(models.Model):
	name = models.CharField(
			default = "",
			max_length = 100,
			help_text = "보드게임 이름을 입력하세요"
		)

	quantity = models.IntegerField(
			default = 1,
			help_text = "수량"
		)

	origin_price = models.IntegerField(
			default = 0,
			help_text = "원래 금액 / 모르면 0원"
		)

	price = models.IntegerField(
			default = 0,
			help_text = "판매 금액"
		)

	image = models.ImageField(
			upload_to = 'images/boardGames', 
			blank = True, 
			null = True,
			help_text='보드게임의 이미지를 업로드하세요'
		)

	people = models.ManyToManyField(
			Person,
			blank = True,
			help_text = '해당 보드게임을 선택한 사람들의 목록입니다.'
		)


	def __str__(self):
		return self.name

class Furniture(models.Model):
	name = models.CharField(
			default = "",
			max_length = 100,
			help_text = "가구 이름을 입력하세요"
		)

	quantity = models.IntegerField(
			default = 1,
			help_text = "수량"
		)

	origin_price = models.IntegerField(
			default = 0,
			help_text = "원래 금액 / 모르면 0원"
		)

	price = models.IntegerField(
			default = 0,
			help_text = "판매 금액"
		)

	image = models.ImageField(
			upload_to = 'images/furniture', 
			blank = True, 
			null = True,
			help_text='가구의 이미지를 업로드하세요'
		)

	people = models.ManyToManyField(
			Person,
			blank = True,
			help_text = '해당 가구를 선택한 사람들의 목록입니다.'
		)


	def __str__(self):
		return self.name

class ETC(models.Model):
	name = models.CharField(
			default = "",
			max_length = 100,
			help_text = "이름을 입력하세요"
		)

	quantity = models.IntegerField(
			default = 1,
			help_text = "수량"
		)

	origin_price = models.IntegerField(
			default = 0,
			help_text = "원래 금액 / 모르면 0원"
		)

	price = models.IntegerField(
			default = 0,
			help_text = "판매 금액"
		)

	category = models.CharField(
			default = "",
			max_length = 100,
			help_text = "물품의 종류를 입력하세요"
		)

	image = models.ImageField(
			upload_to = 'images/etc', 
			blank = True, 
			null = True,
			help_text='이미지를 업로드하세요'
		)

	people = models.ManyToManyField(
			Person,
			blank = True,
			help_text = '해당 물품을 선택한 사람들의 목록입니다.'
		)


	def __str__(self):
		return self.name

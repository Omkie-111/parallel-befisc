.DEFAULT_GOAL := install

install:
	#install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	#format code
	black ./**/*.py 
lint:
	#to check the code has proper syntax or not flake8 or pylint	
	pylint --disable=R,C ./**/*.py 
test:
	#test where m is the marker and vv is the verbose with cov as coverage
build:
	#build container
	docker build -t befisc .
run:
	#run docker
	docker run befisc:latest
deploy:
	#deploy
all: install format lint test build deploy 
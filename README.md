# beloved-waffle
> Idea/inspiration comes from [wopian/kitsu-popular-grabber][0]

Grabs most popular/highest rated shows on [Kitsu][1]

## Requirements
* [Python][2] - 2.7.13
* [Requests][3] - 2.13.0

## Setup
1. Clone git respository:
	``` 
	git clone https://github.com/GHOSTBEAR/beloved-waffle.git
	cd beloved-waffle
	```
1. Install requirements:
	```
	# Goes from that you have Python installed already
	pip install requests
	```
1. Run the script: 
	```
	python beloved.py [-h] [-g GENRE] [-l LIMIT] [-y YEAR] [-s SORT]
	```

## License
All code released under the [Unlicense][4]

[0]:https://github.com/wopian/kitsu-popular-grabber
[1]:https://kitsu.io
[2]:https://www.python.org
[3]:http://docs.python-requests.org/en/master/
[4]:https://github.com/GHOSTBEAR/beloved-waffle/blob/master/LICENSE.md

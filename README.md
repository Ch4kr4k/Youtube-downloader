# Simple Youtube Downloader for linux

- first of all create a directory Video inside a download folder

      cd ~/Downloads
      mkdir Video

##### installation of dependencies

    	pip3 install -r requirements.txt

if pip install -r requirements.txt doesnt work do this

    	pip3 install ffmpeg-python
    	pip3 install pytube

#### linking the executable libraries

    	sudo ln pytd /usr/local/bin

##### usage

    	pytd https://www.youtube.com/watch?v=dQw4w9WgXcQ

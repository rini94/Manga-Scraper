#Rini94
#Download chapters from fanfox.net - Give the chapter limit as argument or else it downloads the entire series

import urllib.request
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

page_count = 0
max_fail_count = 1000 #total failures allowed in a single run
fail_count = 0
count = 0
image_chapter = None
chapters_count = 1
max_chapters = 1500


def get_url ():
	chapter_url = input ("Enter the url of the chapter or the page: \n")
	#chapter_url = "https://fanfox.net/manga/gintama/v77/c704/1.html"
	if len(chapter_url) <= 1:
		print ("\nNo chapter url entered...\nExiting...\n")
		sys.exit()

	if not chapter_url.startswith ("http"):
		chapter_url = "https://" + chapter_url

	if not chapter_url.endswith ("html"):
		if not chapter_url.endswith ("/"):
			chapter_url = chapter_url + "/"
		chapter_url = chapter_url + "1.html"
	return chapter_url


def create_and_change_dir (dir_name):
	file_path = os.path.dirname(os.path.realpath(__file__))+ "/"+dir_name+"/"
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	os.chdir(file_path)


def download_image (image):
	global image_chapter, chapters_count
	try:
		image_url = image.get_attribute('src')
		name = image_url.split('?')
		name1 = name[0].split('/')
		image_name = name1[len(name1) - 1]
		chapter = name1[len(name1) - 3]

		if image_chapter is None:
			image_chapter = chapter
		elif image_chapter != chapter:
			image_chapter = chapter
			next_chapter = driver.current_url.split('/')
			next_chapter_name = next_chapter[len(next_chapter) - 2]
			chapters_count += 1
			if chapters_count > max_chapters:
				return "end"
			print ("Downloading chapter: ",  next_chapter_name)
			create_and_change_dir ("../"+next_chapter_name)
		
		if last_page():
			return "end"

		if ".jpg" in image_url:
			urllib.request.urlretrieve(image_url, image_name)
			print ("Downloaded page: ",  image_name)
			return "success"
		else:
			driver.implicitly_wait(1)

	except Exception as e:
		print ("Exception", e)
		driver.implicitly_wait(1)


def last_page ():
	try:
		return driver.find_element_by_class_name("reader-win-last").value_of_css_property("display") == "block"
	except NoSuchElementException:
		return False


#start
chapter_url = get_url ()

print ("\nLoading...\n")

if len(sys.argv) > 1:
	try:
		max_chapters = int(sys.argv[1])
	except:
		print ("Non number given... No chapter limit set...")

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(chapter_url)

chapter = chapter_url.split('/')
chapter_name = chapter[len(chapter) - 2]

print("Downloading chapter: ",chapter_name)
create_and_change_dir (chapter_name)

while max_fail_count > fail_count:
	image = driver.find_element_by_class_name("reader-main-img")
	download = download_image(image)
	if download == "success":
		count = count + 1
		image.click()
	elif download == "end":
		break
	else:
		fail_count = fail_count + 1

print ("total failures: ", fail_count)
print ("total successes: ", count)
print ("Completed.")

sys.exit()

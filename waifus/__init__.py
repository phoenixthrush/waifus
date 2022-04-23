# MIT License

# Copyright (c) 2022 Phoenixthrush UwU

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = "Phoenixthrush UwU"
__version__ = "1.0.0"
__license__ = "MIT License"

""" Notes:

I just hope that everything works as intended now.
Hope that you enjoy this program.
If you find any bugs, please make a pull request.
Take it easy.

I'm ouda here


"""

import argparse, requests, re, random, string, tkinter, os, time, shutil
from PIL import Image, ImageTk

def getting_user_selection(meow = "no", nsfw = "no"):
    # getting user selection
    if meow == "yes" and nsfw == "no":
        source = "https://api.waifu.pics/sfw/neko"
    elif meow == "yes" and nsfw == "yes":
        source = "https://api.waifu.pics/nsfw/neko"
    elif not meow == "yes" and nsfw == "no":
        source = "https://api.waifu.pics/sfw/waifu"
    elif not meow == "yes" and nsfw == "yes":
        source = "https://api.waifu.pics/nsfw/waifu"

    return source

def getting_url(source):
    # getting image url from source
    data = requests.get(source).text

    # checking if the API rate limit is reached
    if data == "Rate exceeded.":
        raise "API rate limit reached"

    # converting data to a url
    image_url = re.search("(?P<url>https?://[^\s]+)", data).group("url")[:-2]

    # returning image url
    return image_url

def creating_directory(custom_path = "."):
    # changing directory if custom path is set
    try:
        os.chdir(custom_path)
    except FileNotFoundError:
        # if the directory doesn't exist, creating it
        os.mkdir("waifus")
        os.chdir("waifus")

    # creating a directory for the image
    if not os.path.exists("waifus"):
        os.mkdir("waifus")

    # changing directory to the waifus directory if not already there
    if os.path.exists("waifus"):
        os.chdir("waifus")

def save_image(url):
    # getting image from url
    image = requests.get(url)

    # creating a 16 character random string
    global file_name
    file_name = f"{''.join(random.choices(string.ascii_letters + string.digits, k=16))}.png"

    # saving image to current directory
    with open(file_name, "wb") as f:
        f.write(image.content)

def view_image(file_name, sleeping_time):
    # creating a tkinter window
    window = tkinter.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # resizing the image
    source_image = Image.open(file_name)
    image_ratio = min(screen_width/source_image.width, screen_height/source_image.height)
    image_resized = source_image.resize((int(source_image.width*image_ratio), int(source_image.height*image_ratio)))
    final_image = ImageTk.PhotoImage(image_resized)
    
    panel = tkinter.Label(window, image=final_image)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.minsize(width=screen_width, height=screen_height)

    # showing the image
    window.after(sleeping_time * 1000, lambda: window.destroy())
    window.bind('<Escape>', lambda e: window.destroy())
    window.title("Waifus - by Phoenixthrush")
    window.mainloop()

def delete_image(displaying):
    # deleting the image 
    if displaying == "yes":
        # deleting the path of the image
        time.sleep(1)

        # changing directory
        os.chdir("..")

        # deleting the image path
        shutil.rmtree('waifus')

def interating(only_link = "no", custom_path = ".", displaying = "yes", count = 1, meow = "no", nsfw = "no", sleeping_time = 3, deleting = "yes"):
    # getting the image url if only_link is set to yes
    if only_link == "yes":
        url = getting_url(getting_user_selection(meow, nsfw))
        print("Image url: " + url)
        return url

    # changing directory
    creating_directory(custom_path)

    # if displaying is set to yes
    if displaying == "yes":
        # iterating x times
        for i in range(count):
            # saving the image
            save_image(getting_url(getting_user_selection(meow, nsfw)))

            # showing the image
            view_image(file_name, sleeping_time)
    else:
        # iterating x times
        print("\nDownloading images...\n")
        for i in range(count):
            save_image(getting_url(getting_user_selection(meow, nsfw)))
            print(f"{i+1}/{count}")

    # deleting the image if set to yes
    if deleting == "yes":
        delete_image(displaying)

def module(only_link = "no", custom_path = ".", displaying = "yes", count = 1, meow = "no", nsfw = "no", sleeping_time = 3, deleting = "yes"):
    # catching a keyboard interrupt
    try:
        interating(only_link = only_link, custom_path = custom_path, displaying = displaying, count = count, meow = meow, nsfw = nsfw, sleeping_time = sleeping_time, deleting = deleting)
        exit()

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()

if __name__ == "__main__":
    # catching a keyboard interrupt
    try:
        # creating the parser
        parser = argparse.ArgumentParser(description="A simple program to get waifus from https://waifu.pics")
        
        parser.add_argument("-l", "--link", help="only get the image url", required=False)
        parser.add_argument("-p", "--custom_path", help="set a custom path for the image", type=str, required=False)
        parser.add_argument("-d", "--display", help="display the image", required=False)
        parser.add_argument("-c", "--count", help="set the number of images to get", type=int, required=False)
        parser.add_argument("-m", "--meow", help="get an neko image", required=False)
        parser.add_argument("-n", "--nsfw", help="get an nsfw image", required=False)
        parser.add_argument("-t", "--sleeping_time", help="set the sleeping time between images", type=int, required=False)
        parser.add_argument("-r", "--remove", help="remove the image after viewing", required=False)
        
        args = parser.parse_args()

        # making the args default if not set
        if args.link == None:
            args.link = "no"
        if args.custom_path == None:
            args.custom_path = "."
        if args.display == None:
            args.display = "yes"
        if args.count == None:
            args.count = 1
        if args.meow == None:
            args.meow = "no"
        if args.nsfw == None:
            args.nsfw = "no"
        if args.sleeping_time == None:
            args.sleeping_time = 3
        if args.remove == None:
            args.remove = "yes"

        # running the program
        interating(only_link = args.link, custom_path = args.custom_path, displaying = args.display, count = args.count, meow = args.meow, nsfw = args.nsfw, sleeping_time = args.sleeping_time, deleting = args.remove)

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
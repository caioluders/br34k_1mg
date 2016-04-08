import mmap , sys , os , random , Tkinter , time
from PIL import Image , ImageTk

root = Tkinter.Tk() 


def clear() :
	for widget in root.winfo_children():
	    widget.destroy()

def key(event) :
	clear()
	br34k("temp.jpg",random.randint(0,255))
	sh0w("temp.jpg")


def reset(event) :
	python = sys.executable
	os.execl(python, python, * sys.argv)

def br34k(fn,x) :
	f = open(fn,"a+")
	m = mmap.mmap(f.fileno(),0)

	m[random.randint(0,len(m)-1)] = chr(x)

	m.close()
	f.close()


def sh0w(fn) :
	root.update()
	try :
		im = Image.open(fn)
		im.thumbnail((500,500))
		tk_im = ImageTk.PhotoImage(im)
		label = Tkinter.Label(root,image=tk_im,height=500,width=500)
		label.pack()
		root.bind('<Return>', key)
		root.bind('r' , reset)
		root.wm_attributes("-topmost", 1)
		root.mainloop()
		im.close()
	except :
		reset(1)

def main() :
	if ( len(sys.argv) < 2 ) :
		print "Missing name of the file => $ br34k_jpg.py filename.jpg "
	else :
		os.system("cp "+sys.argv[1]+" temp.jpg") # Command injection lols
		sh0w("temp.jpg")
		br34k( "temp.jpg", random.randint(0,255) )
	

if __name__ == "__main__" :
	main()

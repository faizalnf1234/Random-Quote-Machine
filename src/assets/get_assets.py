import urllib.request
from configparser import ConfigParser
import os
import shutil
 
def path():
    global userdl_path,usermv_path
    try :
        config_object = ConfigParser()
        config_object.read("config.ini")
        config = config_object["USERPATH"]
        userdl_path = config["dl_path"]
        usermv_path = config["mv_path"]
 
        print("path ready")
        print("path download :"+userdl_path)
        print("path migrasi :"+usermv_path)
        print("\n")
    except:
        print("path not yet set")
        userdl_path = str(input("Insert Path Download : "))
        usermv_path = str(input("Insert Path Migrate : "))
        config_object["USERPATH"] = {
            "dl_path": userdl_path,
            "mv_path": usermv_path,
        }
        with open('config.ini', 'w') as conf:
            config_object.write(conf)
            print("config file writed")
 
def save(url_hunt):
    down_url = url_hunt
    #userdlnew_path = userdl_path
    #save_loc = userdlnew_path+"/"+down_url.split("/")[-1]
    userdlnew_path = userdl_path.replace('/', '\\ ')
    save_loc = userdlnew_path+"\\"+down_url.split("/")[-1]
    urllib.request.urlretrieve(down_url,save_loc)
 
def paste(condition):
    while True :
        user_url = str(input("Paste Url Here : "))
        save(user_url)
        ask = str(input("Do You Want To Paste Again ? (y/n)"))
        if (ask == "y"):
            continue

        elif (ask == "n"):
         fask = str(input("Do You Want To Migrate File ? (y/n"))
         if (fask == "y"):
            migrate()
         elif (fask == "n"):
            break

        return ask 

def migrate():
    #usermvnew_path = usermv_path
    usermvnew_path = usermv_path.replace('/', '\\ ')
    os.chdir(usermv_path)
    list = os.listdir(usermvnew_path)

    x=1
    ttk="."
    print("\n")
    print("=======[List Migrate File]=======")
    for i in list:
        print(str(x)+ttk+i)
        x=x+1
    print("===============================")
    ask2 = int(input("Select Number Of File To Migrate ?"))
    if (ask2 > 0):
        ask2new = ask2-1
        #mv = usermvnew_path+'/'+list[ask2new]
        mv = usermvnew_path+'\\'+list[ask2new]
        try :
            shutil.move(mv,userdl_path)
            print("file moved.. \n")
        except Exception as e :
            print("Oops!", e.__class__, "occurred.")
            print(e)
        ask3 = str(input("Do You Want To Move File Again ? (y/n)"))
        if (ask3 == "y" ):
            migrate()

        elif (ask3 == "n"):
            fask =  str(input("Do You Want To Direct Save File ? (y/n)"))
            if (fask == "y"):
                paste("y")
            

    elif (ask2 == 0):
        #mv = usermvnew_path+'/'+list[ask2new]
        mv = usermvnew_path+'\\'+list[ask2new]
        shutil.move(mv,userdl_path)
        try :
            shutil.move(mv,userdl_path)
        except Exception as e :
            print("Oops!", e.__class__, "occurred.")
            print(e)
        ask3 = str(input("Do You Want To Move File Again ? (y/n)"))
        if (ask3 == "y" ):
            migrate()

        elif (ask3 == "n"):
            fask =  str(input("Do You Want To Direct Save File ? (y/n)"))
            if (fask == "y"):
                paste("y")
            

 
if __name__=="__main__":
    path()
    menu = str(input("Save To Path or Migrate Download? (dl/mv) "))
    if (menu == "dl"):
        default = "y"
        paste(default)
    elif (menu == "mv"):
        migrate()
    else:
        print("Your Input False \n")

    
   

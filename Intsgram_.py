import instaloader
profile_name = input("Enter your instaram username : ")
print("Downloading media...!")
instaloader.Instaloader().download_profile(profile_name,profile_pic_only=False)
print("Download Completed")

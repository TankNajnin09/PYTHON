# downloading an image from Internet 
import urllib.request 
#copy the image url 
url = "https://kscpac.ac.in/upload/2/newphotogalary_images/m_39.jpg"
#download the image as myimage.jpg in curent directory 
download = urllib.request.urlretrieve(url, "myimage1.jpg")

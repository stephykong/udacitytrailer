import fresh_tomatoes
import media
import webbrowser


Wonder_Woman=media.Movie("Wonder Woman","A strong heroic woman","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://www.youtube.com/watch?v=VSB4wGIdDwo")
print Wonder_Woman.title #wonder title of the film
print Wonder_Woman.storyline  #what it is about
print Wonder_Woman.poster_image_url #poster image
print Wonder_Woman.trailer_youtube_url #youtube trailer
#prints out Wonder_Woman trailer

The_Dark_Knight=media.Movie("The Dark Knight","abandoned boy turned vigilante","https://resizing.flixster.com/N7hdKS6GyTvIOqV7Apu9kTLS1hc=/206x305/v1.bTsxMTE2NzgzNTtqOzE3NTg5OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=1T__uN5xmC0")
print The_Dark_Knight.title #prints out title
print The_Dark_Knight.storyline #what it is about prints out
print The_Dark_Knight.poster_image_url #poster image
print The_Dark_Knight.trailer_youtube_url #prints out link to trailer
#prints out The Dark Knight

Arrow=media.Movie("Green Arrow","Bachelor Turned Hero","https://i.pinimg.com/originals/9f/09/d0/9f09d0dcae10e9c97fa3c177853863fc.jpg","https://www.youtube.com/watch?v=XQS7JkQmlx8")
print Arrow.title #prinout title of film
print Arrow.storyline #prints out what it is about
print Arrow.poster_image_url #prints out the image associated
print Arrow.trailer_youtube_url #prints out the trailer link
#Prints out the Arrow

SoulSurfer=media.Movie("Soul Soul Surfer","Young Woman loses Arm and shows resilience","http://is4.mzstatic.com/image/thumb/Video6/v4/bc/86/e9/bc86e952-cb11-1197-c387-36d138f726e2/source/1200x630bb.jpg","https://www.youtube.com/watch?v=MWeOjBCi3c4")
print SoulSurfer.title #prints out the tile
print SoulSurfer.storyline #prints out the descriptive storyline
print SoulSurfer.poster_image_url #prints out the iamge associated with it
print SoulSurfer.trailer_youtube_url #prints out youtube
#Prints Out Soul Surfer

movies=[Wonder_Woman,Arrow, The_Dark_Knight,SoulSurfer]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.valid_ratings)

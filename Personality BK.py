import webbrowser as wb
points = 0
import time as t
import pyautogui as pg

name = pg.prompt("What is your name? ").title()
if name == "Betsy":
    pg.alert (" yoooo thats my name!")
    points += 10
    t.sleep(1)
    wb.open ("https://static.boredpanda.com/blog/wp-content/uuuploads/cute-baby-animals-2/cute-baby-animals-2-2.jpg")
elif name == "Sarah":
    pg.alert (name + " you are a really person and I am friends with you")
    points += 1
    t.sleep(1)
    wb.open ("https://www.verywellmind.com/thmb/eEedIpGz-wwUT7MamavsbOF1ehw=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/iStock-619961796-edit-59cabaf6845b3400111119b7.jpg")
elif name == "Simon":
    pg.alert (" you are in my comp sci class and you are really good at gymnastics")
    points += 1
    t.sleep(1)
    wb.open ("https://i.pinimg.com/originals/a1/72/d8/a172d8325a334ba26295002069973eed.jpg")
elif name == "Caroline":
    pg.alert (" you are in my comp sci class")
    points += 1
    t.sleep(1)
    wb.open ("https://toije35938.i.lithium.com/t5/image/serverpage/image-id/1663i87DC785D4C51B258/image-size/large?v=1.0&px=999")
elif name == "Ryan":
    pg.alert (" you are in my comp sci class")
    points += 1
    t.sleep(1)
    wb.open ("https://images.vice.com/vice/images/articles/meta/2015/05/28/why-do-i-want-to-crush-cute-animals-1432782372.jpg?crop=1xw%3A0.8162681912681913xh%3Bcenter%2Ccenter&resize=650%3A*&output-quality=55")
elif name == "Owen":
    pg.alert (" you are in my comp sci class")
    points += 1
    t.sleep(1)
    wb.open ("https://i.ytimg.com/vi/qQ5SR0TGSmE/maxresdefault.jpg")
elif name == "Brooks":
    pg.alert (" you are in my comp sci class")
    points += 1
    t.sleep(1)
    wb.open ("http://www.slate.com/content/dam/slate/blogs/wild_things/2015/09/02/150902_WILD_CutePenguins.jpg.CROP.promo-xlarge2.jpg")
else:
    pg.alert (" Hello!")
    points += 1
    t.sleep(1)
    wb.open ("https://vignette.wikia.nocookie.net/animal-jam-clans-1/images/d/d4/Cute-animal-wallpapers-hd-wild-life-photos-pet-images-lovely-animals-hairy-claws-amazing-eyes-cool-884x627.jpg/revision/latest?cb=20160123042737")

game = pg.prompt ("What is your favorite game? ").title()
if game == "Noodle":
    pg.alert (" ha! I already beat it... hehehehehehe")
    t.sleep(1)
    wb.open("https://cdn3s.iosnoops.com/wp-content/uploads/appsicons/1423527464xscreen1.jpg")
    points += 100
elif game == "Forza Motor Sport":
    pg.alert (" that game is pretty dope but noodle is better")
    points += 10
    t.sleep(1)
    wb.open("https://static-ie.gamestop.ie/images/products/261251/3max.jpg")
elif game == "Candy Crush":
    pg.alert (" that game is so hard")
    points += 10
    t.sleep(1)
    wb.open("https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Candy_Crush_Saga_game_setup_example.jpg/220px-Candy_Crush_Saga_game_setup_example.jpg")
elif game == "Pac Man":
    pg.alert (" that game is so fun!!!")
    points += 10
    t.sleep(1)
    wb.open("https://images-na.ssl-images-amazon.com/images/I/71ipTP6sGFL._SY679_.jpg")
elif game == "Fortnite":
    pg.alert (" ewwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    t.sleep(1)
    points -= 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    wb.open("https://cdn.vox-cdn.com/thumbor/T66Qb9FJPnABmLA1rbURIqaWo5E=/0x0:1098x628/1200x800/filters:focal(445x36:619x210)/cdn.vox-cdn.com/uploads/chorus_image/image/61520123/fortnite_supply_llama.0.jpg")
elif game == "Geometry Dash":
    pg.alert (" OMG IM SOOOOO BAD AT THAT GAME I BEAT A LEVEL ON AVERAGE EVERY 2 YEARS")
    points += 10
    t.sleep(1)
    wb.open("https://www.youtube.com/watch?v=TNyhP4p-Nv8")
else:
    pg.alert ("why would you play that Noodle is the best!")
    points += 1
    t.sleep(1)
    wb.open ("https://cms.splendidtable.org/sites/default/files/styles/w2000/public/noodleWok.jpg?itok=H7XoM2vf")

color = pg.prompt ("What is yout favorite color? ").lower()
if color == "purple":
    pg.alert (" my favorite")
    points += 10
    t.sleep(1)
    wb.open("https://i1.sndcdn.com/artworks-000145101045-6u1wy8-t500x500.jpg")
elif color == "lavender":
    pg.alert (" even better!")
    points += 100
    t.sleep(1)
    wb.open("https://i.pinimg.com/originals/c2/8e/03/c28e03e3bac74b6d80cb07ddaf0e8982.jpg")
elif color == "yellow":
    pg.alert (" that is cool")
    points += 1
    t.sleep(1)
    wb.open("https://colourlex.com/wp-content/uploads/2015/10/Lemon_yellow_Lipscher_Weber_225-2-opt.jpg")
elif color == "green":
    pg.alert (" That's my brother's favorite color!")
    points += 1
    t.sleep(1)
    wb.open("https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flag_of_Libya_%281977%E2%80%932011%29.svg/300px-Flag_of_Libya_%281977%E2%80%932011%29.svg.png")
elif color == "orange":
    pg.alert (" thats a bright color....")
    points += 1
    t.sleep(1)
    wb.open("https://d3npzzrehyahmo.cloudfront.net/images/c2/9e/c29e58267e030dbfde208e39c0c72a19_1213791555e_t.png")
elif color == "blue":
    pg.alert (" ooooooooooooooo Sarah's favorite color")
    points += 1
    t.sleep(1)
    wb.open("https://cdn-image.travelandleisure.com/sites/default/files/styles/1600x1000/public/blue0517.jpg?itok=V3825voJ")
else:
    pg.alert ("uh purple is much better...")
    points += 1
    t.sleep(1)
    wb.open("https://sd.keepcalm-o-matic.co.uk/i/purple-is-just-too-awesome.png")

water = pg.prompt ("what is your favortie water brand? ").title()
if water == "Life Water":
    pg.alert ("yusss but it must have a flip cap")
    points += 10
    t.sleep(1)
    wb.open("https://dowserwater.com/wp-content/uploads/2017/06/Screen-Shot-2017-06-05-at-3.53.56-PM-e1505674166574.jpg")
elif water == "poland spring":
    pg.alert ("thats ok")
    points += 1
    t.sleep(1)
    wb.open("https://www.nestle.com/Asset-Library/PublishingImages/Brands/Bottled-Water/polandspring_detail.jpg")
elif water == "Evian":
    pg.alert ("oooooooooo")
    points += 1
    t.sleep(1)
    wb.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_rIB8JV5qSTa_iBxFDvvJQnQ1Sgt4XILmsx6MTk-aYMF9WhiQBOL2lo9L")
elif water == "Fiji":
    pg.alert ("thats ok")
    points += 1
    t.sleep(1)
    wb.open ("https://pics.drugstore.com/prodimg/418322/900.jpg")
elif water == "Soda Stream":
    pg.alert ("oooooooooooooo I love my soda stream")
    points += 1
    t.sleep(1)
    wb.open ("https://images-na.ssl-images-amazon.com/images/I/71Z874-MLWL._SL1500_.jpg")
elif water == "Water":
    pg.alert ("IT DOES NOT ALL TASTE THE SAME")
    points -= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    t.sleep(1)
    wb.open ("https://www.ecowater.com/wp-content/uploads/2015/07/clear-water-glass.jpg")
else:
    pg.alert ("hrmmmmm")
    points -= 1
    t.sleep(1)
    wb.open ("https://www.ecowater.com/wp-content/uploads/2015/07/clear-water-glass.jpg")

food = pg.prompt ("what is your favortie food? ").lower()
if food == "carbs":
    pg.alert (" yusss carbs are the best")
    points += 1000
    t.sleep(1)
    wb.open("https://www.thechunkychef.com/wp-content/uploads/2017/08/One-Pot-Chicken-Parmesan-Pasta-feat.jpg")
elif food == "pizza":
    pg.alert (" thats ok")
    points += 1
    t.sleep(1)
    wb.open("http://sf2.mariefranceasia.com/wp-content/uploads/sites/7/2015/05/10011867_1112499765494657_5536214622864353459_o-750x410.jpg")
elif food == "pasta":
    pg.alert (" oooooooooo carbs")
    points += 10
    t.sleep(1)
    wb.open("https://www.azgrabaplate.com/wp-content/uploads/Homemade-pasta-with-vodka-sauce1-1.jpg")
elif food == "dessert":
    pg.alert (" mmmmmmmmmmmmmmmm")
    points += 1
    t.sleep(1)
    wb.open("https://timeincsecure-a.akamaihd.net/rtmp_uds/474428695/201709/2582/474428695_5579879045001_5579617529001-vs.jpg?pubId=474428695&videoId=5579617529001")
elif food == "ramen":
    pg.alert (" yummy")
    points += 1
    t.sleep(1)
    wb.open("https://bakerbynature.com/wp-content/uploads/2014/09/IMG_5064-4-2.jpg")
elif food == "candy":
    pg.alert (" I love candy")
    points += 10
    t.sleep(1)
    wb.open("https://images-na.ssl-images-amazon.com/images/I/A15vyeqAetL._SL1500_.jpg")
else:
    pg.alert (" it better have carbs")
    points += 1
    t.sleep(1)
    wb.open ("https://chocolatecoveredkatie.com/wp-content/uploads/2017/01/pasta.jpg")

book = pg.prompt ("What is your favorite book?").title()

if "Harry Potter" in book:
        character = pg.promt ("Which character is your favorite?").title()

        if character == "Harry":
            pg.alert("GRYFFINDOR!!!!!!!!!!!!!!!!!!")
        elif character == "Voldemort":
            pg.alert("his nose looks funny")
        elif character == "Hermione":
            pg.alert ("she is smart")
        elif character == "Ron":
            pg.alert ("he has red hair")
        else:
            pg.alert ("Harry is the best!")

if "To All" in book:
    pg.alert ("PETER KAVINSKY")

ice_cream = pg.confirm ("Which of these flavors is your favorite?", "Chose one", ["chocolate", "vanilla", "strawberry"])

if ice_cream == "vanilla":
    pg.alert ("yummy!")
elif ice_cream == "chocolate":
    pg.alert ("the best!!!")
elif ice_cream == "strawberry":
    pg.aler ("yummy!")
    
    

pg.alert ("You have scored: " + str(points))

    

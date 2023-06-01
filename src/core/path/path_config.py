from .path import path_asset, path_static, path_sheet, path_song, path_sfx

ICON_PATH = path_asset("icon.png")
FONT_PATH = path_asset("VT323-Regular.ttf")

static_config = {
    "tall_squares": path_static("back1.png"),
    "tall_rectangles_light": path_static("back2.png"),
    "tall_rectangles": path_static("back3.png"),

    "black": path_static("black.png"),
    "yellow": path_static("placeholderbg.png"),
    "hills": path_static("0.png"),
    "beach": path_static("1.png"),
    "wall": path_static("2.png"),
    "desert": path_static("3.png"),
    "city": path_static("4.png"),
    "cave_entrance": path_static("5.png"),

    "thick_clouds": path_static("cloud0.png"),
    "thin_clear_clouds": path_static("cloud1.png"),
    "thick_clouds_sparse": path_static("cloud2.png"),
    "thick_clear_clouds": path_static("cloud3.png"),
    "thin_clouds": path_static("cloud4.png"),

    "logo": path_static("logo.png"),
    "arrow_down": path_static("arrowdown.png"),
    "game_over": path_static("gameover.png"),
    "rolled_one": path_static("one.png"),
    "bought": path_static("bought.png"),
    "broke": path_static("broke.png"),
    "refresh": path_static("refresh.png"),
    "chest": path_static("chest.png"),
    "badmc": path_static("badmc.png"),
    "mouse": path_static("mouse.png"),
    "poison": path_static("poison_icon.png"),
    "weakened": path_static("weakened_icon.png"),

    "ground": path_static("ground0.png"),
    "bricks": path_static("bricks.png"),
    "casino": path_static("land0.png"),
    "name": path_static("land1.png"),
    "crate": path_static("land2.png"),

    "inventory_layout": path_static("inventory.png"),
    "text_box": path_static("text600x200.png"),
    "text_box_small": path_static("textsmall.png"),
    "shop": path_static("shop.png"),
    "enemy_hud": path_static("ehub0.png"),
    "menu_hud": path_static("mhub1.png"),
    "player_hud": path_static("phub0.png"),
    "example_hud": path_static("example_hub.png")
}

spritesheet_config = {
    "aaron": [path_sheet("ah120x3x5.png"), 120, 120, 3, 5],
    "aaron_icons": [path_sheet("ah_icon.png"), 100, 100, 2, 4],
    "arca": [path_sheet("arca160x110x3x5.png"), 160, 110, 3, 5],
    "arca_icons": [path_sheet("arca_icon.png"), 100, 100, 2, 4],
    "baduck": [path_sheet("duck180x150x5x5.png"), 180, 150, 5, 5],
    "baduck_icons": [path_sheet("duck_icon.png"), 100, 100, 2, 4],
    "baggins": [path_sheet("baggins110x3x5.png"), 110, 110, 3, 5],
    "baggins_icons": [path_sheet("baggins_icon.png"), 100, 100, 2, 4],
    "bursa": [path_sheet("bursa85x120x3x5.png"), 85, 120, 3, 5],
    "bursa_icons": [path_sheet("bursa_icon.png"), 100, 100, 2, 4],
    "cena": [path_sheet("cena190x100x3x5.png"), 190, 100, 3, 5],
    "cena_icons": [path_sheet("cena_icon.png"), 100, 100, 2, 4],
    "connor": [path_sheet("connor85x100x3x5.png"), 85, 100, 3, 5],
    "connor_icons": [path_sheet("connor_icon.png"), 100, 100, 2, 4],
    "dorita": [path_sheet("dorita130x5x8.png"), 130, 130, 5, 8],
    "dorita_icons": [path_sheet("dorita_icon.png"), 100, 100, 2, 4],
    "ellie": [path_sheet("ellie100x3x5.png"), 100, 100, 3, 5],
    "ellie_icons": [path_sheet("ellie_icon.png"), 100, 100, 2, 4],
    "kiran": [path_sheet("kiran150x3x5.png"), 150, 150, 3, 5],
    "kiran_icons": [path_sheet("kiran_icon.png"), 100, 100, 2, 4],
    "buggi": [path_sheet("buggi3x5x100x100.png"), 100, 100, 3, 5],
    "buggi_icons": [path_sheet("buggi_icon.png"), 100, 100, 2, 4],
    "player": [path_sheet("mc100x3x5.png"), 100, 100, 3, 5],
    "player_icons": [path_sheet("mc_icon.png"), 100, 100, 2, 4],
    "ria": [path_sheet("ria140x3x5.png"), 140, 140, 3, 5],
    "ria_icons": [path_sheet("ria_icon.png"), 100, 100, 2, 4],
    "shopkeeper": [path_sheet("shop45x3x5.png"), 45, 45, 3, 5],
    "shopkeeper_icons": [path_sheet("shop_icon.png"), 100, 100, 2, 4],
    "sosh": [path_sheet("sosh70x140x3x5.png"), 70, 140, 3, 5],
    "sosh_icons": [path_sheet("sosh_icon.png"), 100, 100, 2, 4],
    "square": [path_sheet("square85x3x5.png"), 85, 85, 3, 5],
    "square_icons": [path_sheet("square_icon.png"), 100, 100, 2, 4],
    "wally": [path_sheet("whale200x250x5x5.png"), 200, 250, 5, 5],
    "wally_icons": [path_sheet("wally_icon.png"), 100, 100, 2, 4],
    "wandre": [path_sheet("wandre100x160x3x5.png"), 100, 160, 3, 5],
    "wandre_icons": [path_sheet("wandre_icon.png"), 100, 100, 2, 4],
    "dice1": [path_sheet("1dice85x6x6.png"), 85, 85, 6, 6],
    "dice2": [path_sheet("2dice85x6x6.png"), 85, 85, 6, 6],
    "dice3": [path_sheet("3dice85x6x6.png"), 85, 85, 6, 6],
    "button1": [path_sheet("1button70x3x6.png"), 70, 70, 3, 6],
    "button2": [path_sheet("2button75x500x6x3.png"), 75, 500, 6, 3],
    "button3": [path_sheet("3button70x3x6.png"), 70, 70, 3, 6],
    "button4": [path_sheet("4button50x200x2x3.png"), 50, 200, 2, 3],
    "input": [path_sheet("input75x600x1x2.png"), 75, 600, 1, 2]
}

chunk_config = {
    "back": ["button1", 0, 0, 3],
    "left_arrow": ["button1", 0, 3, 3],
    "music": ["button1", 1, 0, 3],
    "cancel": ["button1", 1, 3, 3],
    "right_arrow": ["button1", 2, 0, 3],
    "confirm": ["button1", 2, 3, 3],
    "campaign": ["button2", 0, 0, 3],
    "inventory": ["button2", 1, 0, 3],
    "load": ["button2", 2, 0, 3],
    "play": ["button2", 3, 0, 3],
    "quit": ["button2", 4, 0, 3],
    "shop": ["button2", 5, 0, 3],
    "equip": ["button3", 0, 0, 3],
    "sell": ["button3", 0, 3, 3],
    "save_icon": ["button3", 1, 0, 3],
    "load_icon": ["button3", 1, 3, 3],
    "unequip": ["button3", 2, 0, 3],
    "sound": ["button3", 2, 3, 3],
    "attack": ["button4", 0, 0, 3],
    "skip_tutorial": ["button4", 1, 0, 3],
    "basic1": ["dice1", 0, 0, 6],
    "basic2": ["dice1", 1, 0, 6],
    "basic3": ["dice1", 2, 0, 6],
    "basic4": ["dice1", 3, 0, 6],
    "basic5": ["dice1", 4, 0, 6],
    "poison1": ["dice1", 5, 0, 6],
    "poison2": ["dice2", 0, 0, 6],
    "poison3": ["dice2", 1, 0, 6],
    "heal1": ["dice2", 2, 0, 6],
    "heal2": ["dice2", 3, 0, 6],
    "heal3": ["dice2", 4, 0, 6],
    "placeholder_die": ["dice2", 5, 0, 6],
    "divider1": ["dice3", 0, 0, 6],
    "divider2": ["dice3", 1, 0, 6],
    "divider3": ["dice3", 2, 0, 6],
    "multiplier1": ["dice3", 3, 0, 6],
    "multiplier2": ["dice3", 4, 0, 6],
    "multiplier3": ["dice3", 5, 0, 6]
}

sound_config = {
    "calm": path_song("calm.mp3"),
    "doma": path_song("doma.mp3"),
    "huh": path_song("huh.mp3"),
    "jong": path_song("jong.mp3"),
    "menu": path_song("menu.mp3"),
    "note": path_song("note.mp3"),
    "ones": path_song("ones.mp3"),
    "somedrums": path_song("somedrums.mp3"),
    "Something": path_song("Something.mp3"),
    "stomp": path_song("stomp.mp3"),
    "stomp2": path_song("stomp2.mp3"),
    "trittle": path_song("trittle.mp3"),
    "trooper": path_song("trooper.mp3"),
    "zins": path_song("zins.mp3"),

    "charge": path_sfx("charge.mp3"),
    "click": path_sfx("click.mp3"),
    "good": path_sfx("good.mp3"),
    "heal": path_sfx("heal.mp3"),
    "one": path_sfx("one.mp3"),
    "poison": path_sfx("poison.mp3"),
    "roll": path_sfx("roll.mp3"),
    "shatter": path_sfx("shatter.mp3"),
    "text": path_sfx("text.mp3")
}

sound_ogg_config = {
    "calm": path_song("calm.ogg"),
    "doma": path_song("doma.ogg"),
    "huh": path_song("huh.ogg"),
    "jong": path_song("jong.ogg"),
    "menu": path_song("menu.ogg"),
    "note": path_song("note.ogg"),
    "ones": path_song("ones.ogg"),
    "somedrums": path_song("somedrums.ogg"),
    "Something": path_song("Something.ogg"),
    "stomp": path_song("stomp.ogg"),
    "stomp2": path_song("stomp2.ogg"),
    "trittle": path_song("trittle.ogg"),
    "trooper": path_song("trooper.ogg"),
    "zins": path_song("zins.ogg"),

    "charge": path_sfx("charge.ogg"),
    "click": path_sfx("click.ogg"),
    "good": path_sfx("good.ogg"),
    "heal": path_sfx("heal.ogg"),
    "one": path_sfx("one.ogg"),
    "poison": path_sfx("poison.ogg"),
    "roll": path_sfx("roll.ogg"),
    "shatter": path_sfx("shatter.ogg"),
    "text": path_sfx("text.ogg")
}

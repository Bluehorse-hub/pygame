import pygame, sys, time, random
from pygame.locals import *

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ設定 
WINDOWADJUST = 1.7
WINDOWWIDTH = 640 * WINDOWADJUST
WINDOWHEIGHT = 480 * WINDOWADJUST

# フレームレート
FPS = 30

# 色
#             R    G    B
PURPLE    = (125,   0, 125)
LIGHTBLUE = (170, 190, 255)
BLUE      = (  0,   0, 255)
RED       = (255,   0,   0)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)
YELLOW    = (255, 255,   0)
WHITE     = (255, 255, 255)

# タイトル関連
PROJECTNAME = 'LunaLegend'
titleX = WINDOWWIDTH / 2
titleY = 150
TITLEFONT= pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 120)
FONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 80)
titleback = pygame.image.load("../mygame/data/title/title5.png")
titleback = pygame.transform.scale(titleback, (WINDOWWIDTH, WINDOWHEIGHT))
title_window = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase001.png")
title_window = pygame.transform.scale(title_window, (600, 300))

# タイトル画面での選択肢
STARTGAME = 'はじめる'
startgameX = WINDOWWIDTH / 2
startgameY = 300
QUITGAME = 'やめる'
quitgameX = WINDOWWIDTH / 2
quitgameY = 400

# スタッフロール関連
STUFFEDROLL = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 80)
END = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 100)
PRESSENTER = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 30)

stafflist = ['スタッフ',
            '〜システム〜',
            'Shungen',
            '〜シナリオ〜',
            'Shungen',
            'ChatGPT',
            '〜グラフィック〜',
            'ぴぽや 様',
            'ぴぽや倉庫 様',
            '鳥橋Den 様',
            'ゲームまてりあるず 様',
            '〜ドット絵変換〜',
            'ドット絵こんばーた 様',
            '〜BGM〜',
            'MusMus 様',
            'ユーフルカ 様',
            '〜SE〜',
            'MusMus 様',
            '効果音ラボ 様',
            '〜フォント〜',
            'フロップデザイン 様',
            '〜スクリプト〜',
            'Shungen',
            '〜QA〜',
            'Shungen',
            '〜制作〜',
            'Shungen'
            ]
staffback = pygame.image.load("../mygame/data/battlebackground2/640x480/pipo-battlebg020.jpg")
staffback = pygame.transform.scale(staffback, (WINDOWWIDTH, WINDOWHEIGHT))

# ストーリー関係　　
STORYROLL = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 40)
storyback = pygame.image.load("../mygame/data/battlebackground2/640x480/pipo-battlebg018.jpg")
storyback = pygame.transform.scale(storyback, (WINDOWWIDTH, WINDOWHEIGHT))
storylist = ['星歴2024年',
             '世界は深刻なエネルギー問題に陥っていた',
             'そんな中、二つの宗教が台頭していた',
             '太陽を信仰するソルリアン教',
             '月を信仰するルナリアン教',
             'ルナリアン教極東支部に属する巫女ルナは',
             '月の神アルゲイアの聖なる力を司る者',
             '彼女は夜の静寂と神秘を愛し',
             '常に月の教えを信者たちに伝えていた',
             '彼女の守護者である騎士シンは',
             '勇猛でありながらも冷静で',
             '常にルナを守り抜く誓いを立てていた',
             'ある夜、ルナリアン教の本部から急報が届いた',
             '太陽を崇拝するソルリアン教の',
             'シスターたちが守る古代兵器が眠る遺跡が発見され',
             'その兵器が両教の均衡を崩しかねないという',
             'ルナとシンは、その遺跡を調査し',
             '兵器を無力化する任務を受けた',
             '彼らが向かう先には一体何が待ち受けているのか...']

trueendlist = ['ルナとシンは無事任務を果たした',
               '古代兵器を手に入れたルナリアン教は',
               'それを持ってソルリアン教を蹂躙した',
               '世界はルナリアン教によって統一された',
               'しかし、世界は貧しいまま',
               '月に祈る日々を送った'
]

trueendback = pygame.image.load("../mygame/data/battlebackground1/640x480/pipo-battlebg003.jpg")
trueendback = pygame.transform.scale(trueendback, (WINDOWWIDTH, WINDOWHEIGHT))

anotherendlist = ['ルナとシンの任務は失敗に終わった',
                  'ルナリアン教は窮地に陥るかと思われた',
                  'しかし、ソルリアン教は古代兵器を用いて',
                  'エネルギー問題を解決すべく',
                  'ルナリアン教に和平を申し出た',
                  'ここに長きにわたる貧困から世界は脱し',
                  '平和な時が訪れた'
]

anotherendback = pygame.image.load("../mygame/data/battlebackground1/640x480/pipo-battlebg007.jpg")
anotherendback = pygame.transform.scale(anotherendback, (WINDOWWIDTH, WINDOWHEIGHT))

# 操作時の定数群
DIRECTION = 0
UP = 1 # 上方向
DOWN = 0 # 下方向
RIGHT = 3 # 右方向
LEFT = 2 # 左方向

mikoAnime = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
BossEnemy = [[0,0,0], [0,0,0]]

# 正面画像              
miko = pygame.image.load("../mygame/data/miko/mikoF1.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[0][0] = miko

miko = pygame.image.load("../mygame/data/miko/mikoF2.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[0][1] = miko

miko = pygame.image.load("../mygame/data/miko/mikoF3.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[0][2] = miko

# 背面画像
miko = pygame.image.load("../mygame/data/miko/mikoB1.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[1][0] = miko

miko = pygame.image.load("../mygame/data/miko/mikoB2.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[1][1] = miko

miko = pygame.image.load("../mygame/data/miko/mikoB3.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[1][2] = miko

# 左向き画像
miko = pygame.image.load("../mygame/data/miko/mikoL1.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[2][0] = miko

miko = pygame.image.load("../mygame/data/miko/mikoL2.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[2][1] = miko

miko = pygame.image.load("../mygame/data/miko/mikoL3.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[2][2] = miko

# 右向き画像
miko = pygame.image.load("../mygame/data/miko/mikoR1.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[3][0] = miko

miko = pygame.image.load("../mygame/data/miko/mikoR2.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[3][1] = miko

miko = pygame.image.load("../mygame/data/miko/mikoR3.png")
miko = pygame.transform.scale(miko, (50, 50))
mikoAnime[3][2] = miko

sister = pygame.image.load("../mygame/data/sister/sisterD2.png")
sister = pygame.transform.scale(sister, (50, 50))

saintlight = pygame.image.load("../mygame/data/map/saintlight.png")
saintlight = pygame.transform.scale(saintlight, (WINDOWWIDTH, WINDOWHEIGHT))

kusa = pygame.image.load("../mygame/data/map/kusa1.png")
kusa = pygame.transform.scale(kusa, (50, 50))

woodLU = pygame.image.load("../mygame/data/map/woodLU.png")
woodLU = pygame.transform.scale(woodLU, (50, 50))

woodRU = pygame.image.load("../mygame/data/map/woodRU.png")
woodRU = pygame.transform.scale(woodRU, (50, 50))

woodLD = pygame.image.load("../mygame/data/map/woodLD.png")
woodLD = pygame.transform.scale(woodLD, (50, 50))

woodRD= pygame.image.load("../mygame/data/map/woodRD.png")
woodRD = pygame.transform.scale(woodRD, (50, 50))

woodLD = pygame.image.load("../mygame/data/map/woodLD.png")
woodLD = pygame.transform.scale(woodLD, (50, 50))

woodLU2 = pygame.image.load("../mygame/data/map/woodLU2.png")
woodLU2 = pygame.transform.scale(woodLU2, (50, 50))

woodLU3 = pygame.image.load("../mygame/data/map/woodLU3.png")
woodLU3 = pygame.transform.scale(woodLU3, (50, 50))

woodRU2 = pygame.image.load("../mygame/data/map/woodRU2.png")
woodRU2 = pygame.transform.scale(woodRU2, (50, 50))

woodRU3 = pygame.image.load("../mygame/data/map/woodRU3.png")
woodRU3 = pygame.transform.scale(woodRU3, (50, 50))

symbolLD = pygame.image.load("../mygame/data/map/symbolLD.png")
symbolLD = pygame.transform.scale(symbolLD, (50, 50))

symbolLU = pygame.image.load("../mygame/data/map/symbolLU.png")
symbolLU = pygame.transform.scale(symbolLU, (50, 50))

symbolRD = pygame.image.load("../mygame/data/map/symbolRD.png")
symbolRD = pygame.transform.scale(symbolRD, (50, 50))

symbolRU = pygame.image.load("../mygame/data/map/symbolRU.png")
symbolRU = pygame.transform.scale(symbolRU, (50, 50))

flower1 = pygame.image.load("../mygame/data/map/flower1.png")
flower1 = pygame.transform.scale(flower1, (50, 50))

flower2 = pygame.image.load("../mygame/data/map/flower2.png")
flower2 = pygame.transform.scale(flower2, (50, 50))

flower3 = pygame.image.load("../mygame/data/map/flower3.png")
flower3 = pygame.transform.scale(flower3, (50, 50))

flower4 = pygame.image.load("../mygame/data/map/flower4.png")
flower4 = pygame.transform.scale(flower4, (50, 50))

status_window = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase006.png")
status_window = pygame.transform.scale(status_window, (600, 200))

comand_window = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase006.png")
comand_window = pygame.transform.scale(comand_window, (250, 200))

lines_window = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase006.png")
lines_window = pygame.transform.scale(lines_window, (600, 200))
LINESFONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 30)
lineslist = ["ルナリアン教の方たちですね", "これがあれば世界は変わります", "...", "どうしても奪うと言うなら", "仕方ないですね", "不本意ですが..."]

battleback = pygame.image.load("../mygame/data/battlebackground1/640x480/pipo-battlebg002.jpg")
battleback = pygame.transform.scale(battleback, (WINDOWWIDTH, WINDOWHEIGHT))

skillname_window = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase006.png")
skillname_window = pygame.transform.scale(skillname_window, (800, 150))
SKILLFONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 50)

battlemiko = pygame.image.load("../mygame/data/miko/mikoL2.png")
battlemiko = pygame.transform.scale(battlemiko, (90, 90))
diemiko = pygame.image.load("../mygame/data/miko/diemiko.png")
diemiko = pygame.transform.scale(diemiko, (90, 90))

battlemoribito = pygame.image.load("../mygame/data/otomo/battleotomoL3.png")
battlemoribito = pygame.transform.scale(battlemoribito, (90, 90))
diemoribito = pygame.image.load("../mygame/data/otomo/dieotomo.png")
diemoribito= pygame.transform.scale(diemoribito, (90, 90))

icon = pygame.image.load("../mygame/data/window_and_cursor/icon2.png")

enemy = pygame.image.load("../mygame/data/enemy/doragon1_2.png")
enemy = pygame.transform.scale(enemy, (518, 393))
BossEnemy[0][0] = enemy
BossEnemy[0][1] = 100
BossEnemy[0][2] = 175

enemy = pygame.image.load("../mygame/data/enemy/kyubi1_2.png")
BossEnemy[1][0] = enemy
BossEnemy[1][1] = 100
BossEnemy[1][2] = 175

kishicutin = pygame.image.load("../mygame/data/cutin/kishicutin.png")
kishicutin = pygame.transform.scale(kishicutin, (355*3.5, 45*3.5))

mikocutin = pygame.image.load("../mygame/data/cutin/mikocutin.png")
mikocutin = pygame.transform.scale(mikocutin, (355*3.5, 45*3.5))

gauge = pygame.image.load("../mygame/data/window_and_cursor/pipo-WindowBase001.png")
gauge = pygame.transform.scale(gauge, (200, 25))

wkey = pygame.image.load("../mygame/data/turtorial/w.png")
wkey = pygame.transform.scale(wkey, (50, 50))

akey = pygame.image.load("../mygame/data/turtorial/a.png")
akey = pygame.transform.scale(akey, (50, 50))

skey = pygame.image.load("../mygame/data/turtorial/s.png")
skey = pygame.transform.scale(skey, (50, 50))

dkey = pygame.image.load("../mygame/data/turtorial/d.png")
dkey = pygame.transform.scale(dkey, (50, 50))

enterkey = pygame.image.load("../mygame/data/turtorial/enter.png")
enterkey = pygame.transform.scale(enterkey, (100, 50))

spacekey = pygame.image.load("../mygame/data/turtorial/space.png")
spacekey = pygame.transform.scale(spacekey, (100, 50))

esckey = pygame.image.load("../mygame/data/turtorial/esc.png")
esckey = pygame.transform.scale(esckey, (100, 50))

basicmap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

adjustmap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

eventmap = [
	[8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6],
    [6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8],
    [8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6],
    [6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 15, 10, 12, 15, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 15, 9, 11, 15, 0, 0, 0, 0, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 15, 15, 15, 15, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 6, 8, 6],
    [6, 8, 6, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 8, 6, 8],
    [8, 6, 8, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 6, 8, 6]
]

# 16*26の一枚50*50pxの画像を表示するための定数群
ROW = 17
COL = 22
GS = 50

# 差分画像を順番に選択するための定数
ANIMATIONSPEED = 1

# 戦闘画面関連
OPTIONFONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 40)
DAMAGEFONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 50)
HEALFONT = pygame.font.Font("../mygame/data/Best10-FONT/BestTen-DOT.otf", 50)

ATTACK = 0 # どのコマンドを選択したかの判定
MAGIC = 1
DIFFENCE = 2

ON = 1 # コマンドの強調表示のON・OFF
OFF = 0

justgauge = pygame.image.load("../mygame/data/window_and_cursor/pipo-CursorBase004.png")
justgauge = pygame.transform.scale(justgauge, (50, 600))

# UIの位置に関する定数郡
STATUS_WINDOW_X = 410
STATUS_WINDOW_Y = 600
COMAND_WINDOW_X = 150
COMAND_WINDOW_Y = 600
OPTION_X = 195
OPTION_Y = 625
OPTIONSPACE = 50
ADJUST_X = -50
ADJUST_Y = 0
PLAYER_STATUS_X = 500
PLAYER_STATUS_Y = 625
SKILL_X = 500
SKILL_Y = 625
turtorialhighlightlist = [(705, 270, 80, 125), (990, 10, 70, 620), (COMAND_WINDOW_X - 60, COMAND_WINDOW_Y - 10, 270, 220),(STATUS_WINDOW_X - 60, STATUS_WINDOW_Y - 10, 620, 220) ]
decisionturtoriallist = ["ここから", "戦闘のチュートリアルです", "チュートリアルを見ますか？"]
playerturtoriallist = ["自分のキャラクターです", "上の矢印についている", "キャラを操作しています"]
comandturtoriallist = ["コマンドは3つの中から選びます", "たたかうは通常こうげき", "まほうはルナの", "特殊コマンドで", "複数のスキルを選択できます", "シンのときは", "「わざ」になります", "ぼうぎょは", "ダメージを半減します", "さらにいちばん速く", "行動することができます"]
skillturtoriallist = ["スキルは3つの中から選びます", "左から", "スキル名、威力、消費MPです"]
statusturtoriallist = ["キャラのステータスです", "ひだりがHPでみぎがMP", "おうぎゲージがたまると", "おうぎが使えます", "ゲージは", "たたかう、敵からのこうげき", "さらに、Justgaugeでたまります"]
justgaugeturtoriallist = ["Justgaugeです", "ゲージがMAXのときに", "Enterを押して", "成功すると", "おうぎゲージがたまります"]

class Player:
    def __init__(self, number, hp, mp, attack, diffence, diffencejudge, speed, special):
        self.number = number
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.diffence = diffence
        self.diffencejudge = diffencejudge
        self.speed = speed
        self.special = special

    def damage(self, damage):
        self.hp -= damage

    def skillcost(self, cost):
        self.mp -= cost

    def heal(self, healamount):
        self.hp += healamount

    def gaugeup(self, gaugeamount):
        self.special += gaugeamount
        if self.special > 500:
            self.special = 500

    def gaugereset(self):
        self.special = 0

class Enemy:
    def __init__(self, number, hp, attack, diffence, speed):
        self.number = number
        self.hp = hp
        self.attack = attack
        self.diffence = diffence
        self.speed = speed

    def damage(self, damage):
        self.hp -= damage

    def attackchange(self, change):
        self.attack = change

MIKO = 0
MORIBITO = 1
ENEMY = 2
miko = Player(MIKO, 300, 400, 200, 150, False, 100, 0)
moribito = Player(MORIBITO, 400, 400, 200, 100, False, 300, 0)
enemy = Enemy(ENEMY, 2000, 120, 250, 200)

MIKOSKILL1MP = 20
MIKOSKILL2MP = 30
MIKOSKILL3MP = 35

KISHISKILL1MP = 20
KISHISKILL2MP = 30
KISHISKILL3MP = 40

MIKO_MAXHP = miko.hp
text_MIKO_MAXHP = str(MIKO_MAXHP)

MORIBITO_MAXHP = moribito.hp
text_MORIBITO_MAXHP = str(MORIBITO_MAXHP)

PLAYERNUMBER = 2

ENEMYSKILL = [300, 301, 302, 303, 304, 305]
ENEMYSKILLTOMIKO = [300, 302, 304]
ENEMYSKILLTOMORIBITO = [301, 303, 305]

# 音楽関連
SE = pygame.mixer.Sound("../mygame/data/se/se1.mp3") 
SE.set_volume(0.6)
SE2 = pygame.mixer.Sound("../mygame/data/se/se2.mp3") 
SE.set_volume(0.6)
TITLESE = pygame.mixer.Sound("../mygame/data/se/titlese.mp3") 
TITLESE.set_volume(0.6)
BATTLEBGM = pygame.mixer.Sound("../mygame/data/bgm/battlebgm3.mp3")
BATTLEBGM.set_volume(0.6)
LASTBGM = pygame.mixer.Sound("../mygame/data/bgm/battlebgm2.mp3")
LASTBGM.set_volume(0.6)
TITLEBGM = pygame.mixer.Sound("../mygame/data/bgm/title.mp3")
FIELDBGM = pygame.mixer.Sound("../mygame/data/bgm/field.mp3")
ANOTHERBGM = pygame.mixer.Sound("../mygame/data/bgm/another.mp3")
TRUEBGM = pygame.mixer.Sound("../mygame/data/bgm/true.mp3")
HEAL = pygame.mixer.Sound("../mygame/data/se/heal.mp3")
NORMALSLASH = pygame.mixer.Sound("../mygame/data/se/normalslash.mp3")
SLASH1 = pygame.mixer.Sound("../mygame/data/se/slash1.mp3")
SLASH2 = pygame.mixer.Sound("../mygame/data/se/slash2.mp3")
SWORD = pygame.mixer.Sound("../mygame/data/se/sword.mp3")
NORMALMAGIC = pygame.mixer.Sound("../mygame/data/se/normalmagic.mp3")
LIGHT = pygame.mixer.Sound("../mygame/data/se/light.mp3")
CROW = pygame.mixer.Sound("../mygame/data/se/crow.mp3")
SHIELD = pygame.mixer.Sound("../mygame/data/se/shield.mp3")
DARK = pygame.mixer.Sound("../mygame/data/se/black.mp3")
STAR = pygame.mixer.Sound("../mygame/data/se/star.mp3")
ENCOUNT = pygame.mixer.Sound("../mygame/data/se/encount.mp3")
DEATH = pygame.mixer.Sound("../mygame/data/se/death.mp3")
CUTIN = pygame.mixer.Sound("../mygame/data/se/cutin.mp3")
JUST = pygame.mixer.Sound("../mygame/data/se/just.mp3")
KISHISPECIAL = pygame.mixer.Sound("../mygame/data/se/kishispecial.mp3")
MIKOSPECIAL = pygame.mixer.Sound("../mygame/data/se/mikospecial.mp3")

# スキル関係
SLASHEFFECTSPEED = 15

stareffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
star = pygame.image.load("../mygame/data/skilleffect/star/star1.png")
stareffect[0] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star2.png")
stareffect[1] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star3.png")
stareffect[2] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star4.png")
stareffect[3] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star5.png")
stareffect[4] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star6.png")
stareffect[5] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star7.png")
stareffect[6] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star8.png")
stareffect[7] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star9.png")
stareffect[8] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star10.png")
stareffect[9] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star11.png")
stareffect[10] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star12.png")
stareffect[11] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star13.png")
stareffect[12] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star14.png")
stareffect[13] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star15.png")
stareffect[14] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star16.png")
stareffect[15] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star17.png")
stareffect[16] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star18.png")
stareffect[17] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star19.png")
stareffect[18] = star
star = pygame.image.load("../mygame/data/skilleffect/star/star20.png")
stareffect[19] = star

swordeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword1.png")
swordeffect[0] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword2.png")
swordeffect[1] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword3.png")
swordeffect[2] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword4.png")
swordeffect[3] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword5.png")
swordeffect[4] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword6.png")
swordeffect[5] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword7.png")
swordeffect[6] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword8.png")
swordeffect[7] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword9.png")
swordeffect[8] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword10.png")
swordeffect[9] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword11.png")
swordeffect[10] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword12.png")
swordeffect[11] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword13.png")
swordeffect[12] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword14.png")
swordeffect[13] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword15.png")
swordeffect[14] = sword
sword = pygame.image.load("../mygame/data/skilleffect/sword/sword16.png")
swordeffect[15] = sword

slasheffect = [0, 0, 0, 0, 0, 0, 0, 0, 0]
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash1.png")
slasheffect[0] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash2.png")
slasheffect[1] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash3.png")
slasheffect[2] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash4.png")
slasheffect[3] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash5.png")
slasheffect[4] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash6.png")
slasheffect[5] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash7.png")
slasheffect[6] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash8.png")
slasheffect[7] = slash
slash = pygame.image.load("../mygame/data/skilleffect/slash/slash9.png")
slasheffect[8] = slash

slash2effect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_1.png")
slash2effect[0] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_2.png")
slash2effect[1] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_3.png")
slash2effect[2] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_4.png")
slash2effect[3] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_5.png")
slash2effect[4] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_6.png")
slash2effect[5] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_7.png")
slash2effect[6] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_8.png")
slash2effect[7] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_9.png")
slash2effect[8] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_10.png")
slash2effect[9] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_11.png")
slash2effect[10] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_12.png")
slash2effect[11] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_13.png")
slash2effect[12] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_14.png")
slash2effect[13] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_15.png")
slash2effect[14] = slash2
slash2 = pygame.image.load("../mygame/data/skilleffect/slash2/slash2_16.png")
slash2effect[15] = slash2

slash3effect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_1.png")
slash3effect[0] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_2.png")
slash3effect[1] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_3.png")
slash3effect[2] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_4.png")
slash3effect[3] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_5.png")
slash3effect[4] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_6.png")
slash3effect[5] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_7.png")
slash3effect[6] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_8.png")
slash3effect[7] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_9.png")
slash3effect[8] = slash3
slash3 = pygame.image.load("../mygame/data/skilleffect/slash3/slash3_10.png")
slash3effect[9] = slash3

normalslasheffect = [0, 0, 0, 0, 0, 0, 0, 0, 0]
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash1.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[0] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash2.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[1] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash3.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[2] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash4.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[3] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash5.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[4] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash6.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[5] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash7.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[6] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash8.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[7] = normalslash
normalslash = pygame.image.load("../mygame/data/skilleffect/normalslash/normalslash9.png")
normalslash = pygame.transform.scale(normalslash, (450, 450))
normalslasheffect[8] = normalslash

normalmagiceffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic1.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[0] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic2.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[1] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic3.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[2] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic4.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[3] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic5.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[4] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic6.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[5] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic7.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[6] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic8.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[7] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic9.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[8] = normalmagic
normalmagic = pygame.image.load("../mygame/data/skilleffect/normalmagic/normalmagic10.png")
normalmagic = pygame.transform.scale(normalmagic, (450, 450))
normalmagiceffect[9] = normalmagic

blackeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
black = pygame.image.load("../mygame/data/skilleffect/black/black1.png")
blackeffect[0] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black2.png")
blackeffect[1] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black3.png")
blackeffect[2] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black4.png")
blackeffect[3] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black5.png")
blackeffect[4] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black6.png")
blackeffect[5] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black7.png")
blackeffect[6] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black8.png")
blackeffect[7] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black9.png")
blackeffect[8] = black
black = pygame.image.load("../mygame/data/skilleffect/black/black10.png")
blackeffect[9] = black

croweffect = [0, 0, 0, 0, 0, 0, 0, 0, 0]
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow1.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[0] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow2.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[1] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow3.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[2] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow4.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[3] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow5.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[4] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow6.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[5] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow7.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[6] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow8.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[7] = crow
crow = pygame.image.load("../mygame/data/skilleffect/crow/crow9.png")
crow = pygame.transform.scale(crow, (400, 400))
croweffect[8] = crow

bloodeffect = [0, 0, 0, 0, 0]
blood = pygame.image.load("../mygame/data/skilleffect/blood/blood1.png")
blood = pygame.transform.scale(blood, (400, 400))
bloodeffect[0] = blood
blood = pygame.image.load("../mygame/data/skilleffect/blood/blood2.png")
blood = pygame.transform.scale(blood, (400, 400))
bloodeffect[1] = blood
blood = pygame.image.load("../mygame/data/skilleffect/blood/blood3.png")
blood = pygame.transform.scale(blood, (400, 400))
bloodeffect[2] = blood
blood = pygame.image.load("../mygame/data/skilleffect/blood/blood4.png")
blood = pygame.transform.scale(blood, (400, 400))
bloodeffect[3] = blood
blood = pygame.image.load("../mygame/data/skilleffect/blood/blood5.png")
blood = pygame.transform.scale(blood, (400, 400))
bloodeffect[4] = blood

lighteffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
light = pygame.image.load("../mygame/data/skilleffect/light/light1.png")
lighteffect[0] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light2.png")
lighteffect[1] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light3.png")
lighteffect[2] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light4.png")
lighteffect[3] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light5.png")
lighteffect[4] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light6.png")
lighteffect[5] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light7.png")
lighteffect[6] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light8.png")
lighteffect[7] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light9.png")
lighteffect[8] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light10.png")
lighteffect[9] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light11.png")
lighteffect[10] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light12.png")
lighteffect[11] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light13.png")
lighteffect[12] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light14.png")
lighteffect[13] = light
light = pygame.image.load("../mygame/data/skilleffect/light/light15.png")
lighteffect[14] = light

shieldeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield1.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[0] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield2.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[1] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield3.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[2] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield4.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[3] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield5.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[4] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield6.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[5] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield7.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[6] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield8.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[7] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield9.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[8] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield10.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[9] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield11.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[10] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield12.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[11] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield13.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[12] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield14.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[13] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield15.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[14] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield16.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[15] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield17.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[16] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield18.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[17] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield19.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[18] = shield
shield = pygame.image.load("../mygame/data/skilleffect/shield/shield20.png")
shield = pygame.transform.scale(shield, (200, 200))
shieldeffect[19] = shield

healeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal1.png")
healeffect[0] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal2.png")
healeffect[1] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal3.png")
healeffect[2] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal4.png")
healeffect[3] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal5.png")
healeffect[4] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal6.png")
healeffect[5] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal7.png")
healeffect[6] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal8.png")
healeffect[7] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal9.png")
healeffect[8] = heal
heal = pygame.image.load("../mygame/data/skilleffect/heal/heal10.png")
healeffect[9] = heal

kishispecialeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial1.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[0] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial2.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[1] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial3.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[2] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial4.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[3] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial5.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[4] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial6.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[5] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial7.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[6] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial8.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[7] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial9.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[8] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial10.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[9] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial11.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[10] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial12.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[11] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial13.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[12] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial14.png")
kishispecialeffect[13] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial15.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[14] = kishispecial
kishispecial = pygame.image.load("../mygame/data/skilleffect/kishispecial/kishispecial16.png")
kishispecial = pygame.transform.scale(kishispecial, (WINDOWWIDTH, WINDOWHEIGHT))
kishispecialeffect[15] = kishispecial

mikospecialeffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial1.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[0] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial2.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[1] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial3.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[2] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial4.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[3] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial5.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[4] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial6.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[5] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial7.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[6] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial8.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[7] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial9.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[8] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial10.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[9] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial11.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[10] = mikospecial
mikospecial = pygame.image.load("../mygame/data/skilleffect/mikospecial/mikospecial12.png")
mikospecial = pygame.transform.scale(mikospecial, (WINDOWWIDTH, WINDOWHEIGHT))
mikospecialeffect[11] = mikospecial

encounteffect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
encount = pygame.image.load("../mygame/data/encount/encount1.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[0] = encount
encount = pygame.image.load("../mygame/data/encount/encount2.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[1] = encount
encount = pygame.image.load("../mygame/data/encount/encount3.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[2] = encount
encount = pygame.image.load("../mygame/data/encount/encount4.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[3] = encount
encount = pygame.image.load("../mygame/data/encount/encount5.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[4] = encount
encount = pygame.image.load("../mygame/data/encount/encount6.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[5] = encount
encount = pygame.image.load("../mygame/data/encount/encount7.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[6] = encount
encount = pygame.image.load("../mygame/data/encount/encount8.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[7] = encount
encount = pygame.image.load("../mygame/data/encount/encount9.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[8] = encount
encount = pygame.image.load("../mygame/data/encount/encount10.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[9] = encount
encount = pygame.image.load("../mygame/data/encount/encount11.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[10] = encount
encount = pygame.image.load("../mygame/data/encount/encount12.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[11] = encount
encount = pygame.image.load("../mygame/data/encount/encount13.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[12] = encount
encount = pygame.image.load("../mygame/data/encount/encount14.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[13] = encount
encount = pygame.image.load("../mygame/data/encount/encount15.png")
encount = pygame.transform.scale(encount, (800, 800))
encounteffect[14] = encount

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(PROJECTNAME)

    # 遊び方の説明画面
    ControlTurtorial(SCREEN, FPSCLOCK)

    # 注意書き画面
    Warnig(SCREEN, FPSCLOCK)

    # タイトル画面を描画する関数
    TITLEBGM.play(-1)
    TitleMain(SCREEN, FPSCLOCK)

    # ストーリー画面
    StoryRoll(storylist, storyback, SCREEN, FPSCLOCK)
    TITLEBGM.fadeout(1000)

    # 全体マップ関連
    FieldMain(SCREEN, FPSCLOCK)
    time.sleep(0.3)

    #バトルループ
    Battleresult = BattleLoop(SCREEN, FPSCLOCK)
    if Battleresult == True:
        TRUEBGM.play()
        StoryRoll(trueendlist,trueendback, SCREEN, FPSCLOCK)
    elif Battleresult == False:
        ANOTHERBGM.play()
        StoryRoll(anotherendlist, anotherendback, SCREEN, FPSCLOCK)

    #スタッフロール関数
    StaffedRoll(stafflist, SCREEN, FPSCLOCK)

def TextDraw(msg, font, color, x, y, screen):
    # 任意のテキストを指定した位置に描画する関数
    # msg：表示したい文字列（str）
    # font：文字のフォント（文字サイズは宣言時に指定）
    # color：色（(R, G, B)）
    # x：表示したい箇所のX座標（int）
    # y：表示したい箇所のY座標（int）
    # screen
    text = font.render(msg, True, color)
    textRect = text.get_rect()
    textRect.center = int(x), int(y)
    screen.blit(text, textRect)

def OptionTextDraw(msg, font, color, x, y, screen):
    text = font.render(msg, True, color)
    screen.blit(text, (int(x), int(y)))

def TitleMain(screen, fpsclock):
    # タイトル画面を描画する関数

    # タイトル画面の選択肢の強調表示に使用する定数群
    TITLE_OPTION_COLOR = [WHITE, YELLOW] 
    START_NUMBER = 1
    QUIT_NUMBER = 0
    NOWACTION = 1
    NOTNOWACTION = 0
    
    title_running = True
    TITLEQUIT = False

    alpha1 = 255
    while alpha1 > 0:
        screen.blit(titleback, (0,0))
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha1))
        screen.blit(fade,(0,0))
        pygame.display.update()
        alpha1 -= 5

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

        fpsclock.tick(FPS)

    while title_running: # タイトル画面を描画するループ
        screen.blit(titleback, (0,0))

        # タイトルを描画
        TextDraw(STARTGAME, FONT, TITLE_OPTION_COLOR[START_NUMBER], startgameX,startgameY + 200, screen)
        TextDraw(QUITGAME, FONT, TITLE_OPTION_COLOR[QUIT_NUMBER], quitgameX, quitgameY + 200, screen)

        pygame.display.update()

        if TITLEQUIT == True:
            break

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                title_running = False
                terminate()

            elif event.type == KEYDOWN:
                if event.key == K_s:
                    SE.play()
                    if START_NUMBER == NOWACTION:
                        START_NUMBER = NOTNOWACTION
                        QUIT_NUMBER = NOWACTION
                if event.key == K_w:
                    SE.play()
                    if START_NUMBER == NOTNOWACTION:
                        START_NUMBER = NOWACTION
                        QUIT_NUMBER = NOTNOWACTION
                if event.key == K_RETURN:
                    TITLESE.play()
                    if START_NUMBER == NOTNOWACTION:
                        title_running = False
                        pygame.quit() 
                        sys.exit() 
                    elif START_NUMBER == NOWACTION:
                        TITLEQUIT = True

    fpsclock.tick(FPS)

    alpha2 = 0
    while alpha2 < 255:
        screen.blit(titleback, (0,0))
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha2))
        screen.blit(fade,(0,0))
        pygame.display.update()
        alpha2 += 5

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        fpsclock.tick(FPS)

    return

def draw_basicmap(screen, map):
    for r in range(ROW):
        for c in range(COL):
            if map[r][c] == 0:
                screen.blit(kusa, (c*GS,r*GS))
            
def draw_eventmap(screen, map):
    for r in range(ROW):
        for c in range(COL):
            if map[r][c] == 0:
                screen.blit(kusa, (c*GS,r*GS))
            elif map[r][c] == 1:
                screen.blit(woodLU, (c*GS,r*GS))
            elif map[r][c] == 2:
                screen.blit(woodRU, (c*GS,r*GS))
            elif map[r][c] == 3:
                screen.blit(woodLD, (c*GS,r*GS))
            elif map[r][c] == 4:
                screen.blit(woodRD, (c*GS,r*GS))
            elif map[r][c] == 5:
                screen.blit(woodLU2, (c*GS,r*GS))
            elif map[r][c] == 6:
                screen.blit(woodLU3, (c*GS,r*GS))
            elif map[r][c] == 7:
                screen.blit(woodRU2, (c*GS,r*GS))
            elif map[r][c] == 8:
                screen.blit(woodRU3, (c*GS,r*GS))
            elif map[r][c] == 9:
                screen.blit(symbolLD, (c*GS,r*GS))
            elif map[r][c] == 10:
                screen.blit(symbolLU, (c*GS,r*GS))
            elif map[r][c] == 11:
                screen.blit(symbolRD, (c*GS,r*GS))
            elif map[r][c] == 12:
                screen.blit(symbolRU, (c*GS,r*GS))
            elif map[r][c] == 13:
                screen.blit(flower1, (c*GS,r*GS))
            elif map[r][c] == 14:
                screen.blit(flower2, (c*GS,r*GS))
            elif map[r][c] == 15:
                screen.blit(flower3, (c*GS,r*GS))
            elif map[r][c] == 16:
                screen.blit(flower4, (c*GS,r*GS))
            
def draw_adjustmap(screen, map):
    for r in range(ROW):
        for c in range(COL):
            if map[r][c] == 1:
                screen.blit(woodLU, (c*GS,r*GS))
            elif map[r][c] == 2:
                screen.blit(woodRU, (c*GS,r*GS))
            elif map[r][c] == 3:
                screen.blit(woodLD, (c*GS,r*GS))
            elif map[r][c] == 4:
                screen.blit(woodRD, (c*GS,r*GS))
            elif map[r][c] == 5:
                screen.blit(woodLU2, (c*GS,r*GS))
            elif map[r][c] == 6:
                screen.blit(woodLU3, (c*GS,r*GS))
            elif map[r][c] == 7:
                screen.blit(woodRU2, (c*GS,r*GS))
            elif map[r][c] == 8:
                screen.blit(woodRU3, (c*GS,r*GS))
            elif map[r][c] == 9:
                screen.blit(symbolLD, (c*GS,r*GS))
            elif map[r][c] == 10:
                screen.blit(symbolLU, (c*GS,r*GS))
            elif map[r][c] == 11:
                screen.blit(symbolRD, (c*GS,r*GS))
            elif map[r][c] == 12:
                screen.blit(symbolRU, (c*GS,r*GS))
            elif map[r][c] == 13:
                screen.blit(flower1, (c*GS,r*GS))
            elif map[r][c] == 14:
                screen.blit(flower2, (c*GS,r*GS))
            elif map[r][c] == 15:
                screen.blit(flower3, (c*GS,r*GS))
            elif map[r][c] == 16:
                screen.blit(flower4, (c*GS,r*GS))

def CollisionJudge(px, py, npcx, npcy):
    # 衝突を判定
    # NPCへの食い込み具合を調整するためのもの
    adjustX = 40 
    adjustUPY = 45
    adjustDOWNY = 25

    if (px > npcx - adjustX and px < npcx + adjustX) and (py > npcy - adjustUPY and py < npcy + adjustDOWNY):
        return True
    else:
        return False

def CollisionFromLeftJudge(px, py, npcx, npcy):
    # 左からの衝突を判定
    # 侵入を防ぐ

    # 厚みをつける。1フレーム分の侵入を許容するため
    WALL = 10 

    # NPCへの食い込み具合を調整するためのもの
    adjustX = 40 
    adjustUPY = 45
    adjustDOWNY = 25

    if (px > npcx - adjustX and px < npcx - adjustX + WALL) and (py > npcy - adjustUPY and py < npcy + adjustDOWNY):
        return True
    else:
        return False
    
def CollisionFromRightJudge(px, py, npcx, npcy):
    # 右からの衝突を判定
    # 侵入を防ぐ

    # 厚みをつける。1フレーム分の侵入を許容するため
    WALL = 10

    # NPCへの食い込み具合を調整するためのもの
    adjustX = 40
    adjustUPY = 45
    adjustDOWNY = 25

    if (px > npcx + adjustX - WALL and px < npcx + adjustX) and (py > npcy - adjustUPY and py < npcy + adjustDOWNY):
        return True
    else:
        return False
    
def CollisionFromUpJudge(px, py, npcx, npcy):
    # 上からの衝突を判定
    # 侵入を防ぐ

    # 厚みをつける。1フレーム分の侵入を許容するため
    WALL = 10

    # NPCへの食い込み具合を調整するためのもの
    adjustX = 40
    adjustUPY = 45
    if (px > npcx - adjustX and px < npcx + adjustX) and (py > npcy - adjustUPY and py < npcy - adjustUPY + WALL):
        return True
    else:
        return False
    
def CollisionFromDownJudge(px, py, npcx, npcy):
    # 下からの衝突を判定
    # 侵入を防ぐ

    # 厚みをつける。1フレーム分の侵入を許容するため
    WALL = 10

    # NPCへの食い込み具合を調整するためのもの
    adjustX = 40
    adjustDWONY = 25
    if (px > npcx - adjustX and px < npcx + adjustX) and (py > npcy + adjustDWONY - WALL and py < npcy + adjustDWONY):
        return True
    else:
        return False
    
def FieldMain(screen, fpsclock):
    # メインのループを回すフラグ
    field_running = True

    # 主人公の初期位置
    px = 525
    py = 750

    # １フレームで動くピクセル数
    speed = 5

    # 差分画像の向きを判定するフラグ
    direction = 1

    # 何番目の差分画像かを選択するフラグ
    move = 1

    INTRUSION = True # 侵入可能かどうかを判定するフラグ

    symbolLDX = 500
    symbolLDY = 300

    symbolRDX = 550
    symbolRDY = 300

    symbolLUX = 500
    symbolLUY = 250

    symbolRUX = 550
    symbolRUY = 250

    sisterX = 525
    sisterY = 390

    alpha = 255

    FIELDBGM.play(-1)
    while alpha > 0:
        draw_basicmap(screen, basicmap)
        draw_adjustmap(screen, adjustmap)
        draw_eventmap(screen, eventmap)

        screen.blit(sister, (sisterX, sisterY))

        # 主人公の描画
        # direction：画像の向き
        # move%3：差分画像を順番に選択するための処理
        # (px, py)：描画する座標
        screen.blit(mikoAnime[1][1], (px, py))

        screen.blit(saintlight, (0,0))

        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha))
        screen.blit(fade,(0,0))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
        
        alpha -= 5

        fpsclock.tick(FPS)

    while field_running:
        draw_basicmap(screen, basicmap)
        draw_adjustmap(screen, adjustmap)
        draw_eventmap(screen, eventmap)

        screen.blit(sister, (sisterX, sisterY))

        screen.blit(mikoAnime[direction][move%3], (px, py))

        screen.blit(saintlight, (0,0))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:  
                field_running = False
                terminate()
            
            # 移動を終了した時にIDLE状態の画像に強制変更する処理
            elif event.type == KEYUP:
                move = ANIMATIONSPEED

            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if ((505 < px < 550) and (415 <= py <= 425)) and (direction == UP):
                        SE2.play()
                        screen.blit(lines_window, (250, 10))
                        TextDraw("おや", LINESFONT, WHITE, 550, 110, screen)
                        pygame.display.update() 
                        field_running = False
                        
        # キャラクター操作の処理
        pressed_keys = pygame.key.get_pressed()
        if INTRUSION == True:
            if pressed_keys[K_w]: # 上方向に移動する時の処理
                py -= speed # 移動速度
                direction = UP # 画像の向きの判定
                move += ANIMATIONSPEED # 差分画像の選択
            elif pressed_keys[K_s]: # 下方向に移動する時の処理
                py += speed
                direction = DOWN
                move += ANIMATIONSPEED
            elif pressed_keys[K_a]: # 左方向に移動する時の処理
                px -= speed
                direction = LEFT
                move += ANIMATIONSPEED
            elif pressed_keys[K_d]: # 右方向に移動する時の処理
                px += speed
                direction = RIGHT
                move += ANIMATIONSPEED
        
        # フィールドに対する当たり判定
        if px < 240 or py < 240:
            INTRUSION = False
            if py < 240:
                    py += speed
            elif px < 240:
                    px += speed
        elif px > 810 or py > 760:
            INTRUSION = False
            if py > 760:
                py -= speed
            elif px > 810:
                px -= speed
        else:
            INTRUSION = True

        # 設置物の当たり判定
        if CollisionJudge(px, py, symbolLDX, symbolLDY):
            INTRUSION = False
            if CollisionFromLeftJudge(px, py, symbolLDX, symbolLDY):
                px -= speed
            elif CollisionFromRightJudge(px, py, symbolLDX, symbolLDY):
                px += speed
            elif CollisionFromUpJudge(px, py, symbolLDX, symbolLDY):
                py -= speed
            elif CollisionFromDownJudge(px, py, symbolLDX, symbolLDY):
                py += speed
            else:
                INTRUSION = True    

        if CollisionJudge(px, py, symbolRDX, symbolRDY):
            INTRUSION = False
            if CollisionFromLeftJudge(px, py, symbolRDX, symbolRDY):
                px -= speed
            elif CollisionFromRightJudge(px, py, symbolRDX, symbolRDY):
                px += speed
            elif CollisionFromUpJudge(px, py, symbolRDX, symbolRDY):
                py -= speed
            elif CollisionFromDownJudge(px, py, symbolRDX, symbolRDY):
                py += speed
            else:
                INTRUSION = True

        if CollisionJudge(px, py, symbolLUX, symbolLUY):
            INTRUSION = False
            if CollisionFromLeftJudge(px, py, symbolLUX, symbolLUY):
                px -= speed
            elif CollisionFromRightJudge(px, py, symbolLUX, symbolLUY):
                px += speed
            elif CollisionFromUpJudge(px, py, symbolLUX, symbolLUY):
                py -= speed
            elif CollisionFromDownJudge(px, py, symbolLUX, symbolLUY):
                py += speed
            else:
                INTRUSION = True

        if CollisionJudge(px, py, symbolRUX, symbolRUY):
            INTRUSION = False
            if CollisionFromLeftJudge(px, py, symbolRUX, symbolRUY):
                px -= speed
            elif CollisionFromRightJudge(px, py, symbolRUX, symbolRUY):
                px += speed
            elif CollisionFromUpJudge(px, py, symbolRUX, symbolRUY):
                py -= speed
            elif CollisionFromDownJudge(px, py, symbolRUX, symbolRUY):
                py += speed
            else:
                INTRUSION = True

        # NPCの当たり判定
        if CollisionJudge(px, py, sisterX, sisterY):
            INTRUSION = False
            if CollisionFromLeftJudge(px, py, sisterX, sisterY):
                px -= speed
            elif CollisionFromRightJudge(px, py, sisterX, sisterY):
                px += speed
            elif CollisionFromUpJudge(px, py, sisterX, sisterY):
                py -= speed
            elif CollisionFromDownJudge(px, py, sisterX, sisterY):
                py += speed
            else:
                INTRUSION = True    

        fpsclock.tick(FPS)
    # イベント処理
    if field_running == False:
        FirstEvent(px, py, sisterX, sisterY, screen)
        FIELDBGM.fadeout(100)
        EncountEffect(px, py, sisterX, sisterY, screen, fpsclock)
        return

def terminate():
    # ゲームを終了する関数
    pygame.quit() 
    sys.exit() 

def FinalSelectJudge(player, option, screen):
    selectedskill = -1
    if option == ATTACK:
        if player.special < 500:
            return ATTACK + 10
        elif player.special >= 500:
            player.gaugereset()
            return ATTACK + 50
    elif option == MAGIC:
        SkillUI(player, screen)
        selectedskill = SkillSelect(player ,screen)
        if selectedskill < 0:
            return -1
        elif selectedskill >= 0:
            return selectedskill

        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

    elif option == DIFFENCE:
        return DIFFENCE + 20

def EnemyAttack(player, enemy):
    player.damage(enemy.attack)

def SkillUI(player, screen):
    # スキル選択後の種類選択画面への移行画面の描画

    if player.number == MIKO:
        skilltext = "まほう"
    elif player.number == MORIBITO:
        skilltext = "わざ"
    if miko.special >= 500:
        attacktext = 'おうぎ'
    elif miko.special < 500:
        attacktext = 'たたかう'
    if moribito.special >= 500:
        attacktext = 'おうぎ'
    elif moribito.special < 500:
        attacktext = 'たたかう'

    screen.blit(battleback, (0, 0))

    screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
    screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))

    if miko.hp > 0:
        screen.blit(battlemiko, (700, 300))
    elif miko.hp <= 0:
        screen.blit(diemiko, (700, 300))
    if moribito.hp > 0:
        screen.blit(battlemoribito, (700, 420))
    elif moribito.hp <= 0:
        screen.blit(diemoribito, (700, 420))
    screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))

    JustInputView(screen)

    OptionTextDraw(attacktext, OPTIONFONT, WHITE, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y, screen)
    OptionTextDraw(skilltext, OPTIONFONT, YELLOW, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + OPTIONSPACE, screen)
    OptionTextDraw('ぼうぎょ', OPTIONFONT, WHITE, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + 2*OPTIONSPACE, screen)

def SkillSelect(player, screen):
    now_select = True
    skill_option = ['skill1', 'skill2', 'skill3']
    skill_option_color = [WHITE, YELLOW]
    skill_option_number = 0
    skill1_color = 1
    skill2_color = 0
    skill3_color = 0

    while now_select:

        if player.number == MIKO:
            SelectPlayerIcon(725, 280, screen)
        elif player.number == MORIBITO:
            SelectPlayerIcon(725, 400, screen)

        if player.number == MIKO:
            OptionTextDraw('流星群　　　中　　20', OPTIONFONT, skill_option_color[skill1_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y, screen)
            OptionTextDraw('聖なる剣　　大　　30', OPTIONFONT, skill_option_color[skill2_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + OPTIONSPACE, screen)
            OptionTextDraw('癒しの光　　癒　　35', OPTIONFONT, skill_option_color[skill3_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + 2*OPTIONSPACE, screen)
        elif player.number == MORIBITO:
            OptionTextDraw('壱ノ型　　　小　　20', OPTIONFONT, skill_option_color[skill1_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y, screen)
            OptionTextDraw('弐ノ型　　　中　　30', OPTIONFONT, skill_option_color[skill2_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + OPTIONSPACE, screen)
            OptionTextDraw('参ノ型　　　大　　40', OPTIONFONT, skill_option_color[skill3_color], SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + 2*OPTIONSPACE, screen)

        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_s:
                    SE.play()
                    if skill_option[skill_option_number] == 'skill1':
                        skill_option_number = 1
                        skill1_color = OFF
                        skill2_color = ON
                        skill3_color = OFF
                    elif skill_option[skill_option_number] == 'skill2':
                        skill_option_number = 2
                        skill1_color = OFF
                        skill2_color = OFF
                        skill3_color = ON
                    elif skill_option[skill_option_number] == 'skill3':
                        skill_option_number = 2
                        skill1_color = OFF
                        skill2_color = OFF
                        skill3_color = ON
                elif event.key == K_w:
                    SE.play()
                    if skill_option[skill_option_number] == 'skill2':
                        skill_option_number = 0
                        skill1_color = ON
                        skill2_color = OFF
                        skill3_color = OFF
                    elif skill_option[skill_option_number] == 'skill3':
                        skill_option_number = 1
                        skill1_color = OFF
                        skill3_color = OFF
                        skill2_color = ON
                    elif skill_option[skill_option_number] == 'skill1':
                        skill_option_number = 0
                        skill1_color = ON
                        skill3_color = OFF
                        skill2_color = OFF
                elif event.key == K_RETURN:
                    SE2.play()
                    now_select = False
                    return skill_option_number
                elif event.key == K_ESCAPE:
                    SE2.play()
                    return -1
            elif event.type == QUIT:
                terminate()

def Damage(attackside, diffenceside, skillnumber):
    # 倍率を設定
    correction = 1
    MIKOSKILL1RATE = 2.8
    MIKOSKILL2RATE = 3.3
    KISHISKILL1RATE = 1.9
    KISHISKILL2RATE = 2.6
    KISHISKILL3RATE = 3
    ENEMYSKILL1RATE = 2.8
    ENEMYSKILL2RATE = 2
    ENEMYSKILL3RATE = 2.5
    MIKOSPECIALRATE = 10
    KISHISPECIALRATE = 15
    # skillnumberで指定しダメージを計算
    if skillnumber == 110: # 巫女通常攻撃
        correction = 1
    elif skillnumber == 100: # 巫女流星群
        correction = MIKOSKILL1RATE
        miko.skillcost(MIKOSKILL1MP)
    elif skillnumber == 101: # 巫女剣爆発
        correction = MIKOSKILL2RATE
        miko.skillcost(MIKOSKILL2MP)
    elif skillnumber == 102: # 巫女回復（いじらなくて良い）
        correction = 1
    elif skillnumber == 122: # 巫女ぼうぎょ（いじらなくて良い）
        correction = 1
    elif skillnumber == 150: # 巫女おうぎ
        correction = MIKOSPECIALRATE
    elif skillnumber == 210: # 騎士通常攻撃
        correction = 1
    elif skillnumber == 200: # 騎士青斬撃
        correction = KISHISKILL1RATE
        moribito.skillcost(KISHISKILL1MP)
    elif skillnumber == 201: # 騎士ネオン斬撃
        correction = KISHISKILL2RATE
        moribito.skillcost(KISHISKILL2MP)
    elif skillnumber == 202: # 騎士赤斬撃
        correction = KISHISKILL3RATE
        moribito.skillcost(KISHISKILL3MP)
    elif skillnumber == 222: # 騎士ぼうぎょ（いじらなくて良い）
        correction = 1
    elif skillnumber == 250: # 騎士おうぎ
        correction = KISHISPECIALRATE
    elif skillnumber == 300: # 敵黒棘
        correction = ENEMYSKILL1RATE
    elif skillnumber == 301: # 敵黒棘
        correction = ENEMYSKILL1RATE
    elif skillnumber == 302: # 敵引っ掻き
        correction = ENEMYSKILL2RATE
    elif skillnumber == 303: # 敵引っ掻き
        correction = ENEMYSKILL2RATE
    elif skillnumber == 304: # 敵粒子爆発
        correction = ENEMYSKILL3RATE
    elif skillnumber == 305: # 敵粒子爆発
        correction = ENEMYSKILL3RATE
    basicdamage = ((attackside.attack / 2) - (diffenceside.diffence / 4))
    totaldamage = (basicdamage + random.randint(0,10) - random.randint(0,10)) * correction
    if totaldamage < 0:
        totaldamage = 0
    return int(totaldamage)

def PlayerMove(player, screen, fpsclock):

    if player.number == MIKO:
        skilltext = "まほう"
    elif player.number == MORIBITO:
        skilltext = "わざ"
    if player.special >= 500:
        attacktext = 'おうぎ'
    elif miko.special < 500:
        attacktext = 'たたかう'

    # 戦闘画面の処理
    battle_running = True

    BATTLEQUIT = False

    battle_option = ['attack', 'skill', 'diffence']

    battle_option_color = [WHITE, YELLOW]

    battle_option_number = 0

    attack_color = 1

    skill_color = 0
    
    diffence_color = 0

    #             playername, スキル番号, 素早さ
    playermove = [         0,        0,     0]

    while battle_running:
        screen.blit(battleback, (0, 0))

        screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
        screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))

        if miko.hp > 0:
            screen.blit(battlemiko, (700, 300))
        elif miko.hp <= 0:
            screen.blit(diemiko, (700, 300))
        if moribito.hp > 0:
            screen.blit(battlemoribito, (700, 420))
        elif moribito.hp <= 0:
            screen.blit(diemoribito, (700, 420))
        screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))
        
        if player.number == MIKO:
            SelectPlayerIcon(725, 280, screen)
        elif player.number == MORIBITO:
            SelectPlayerIcon(725, 400, screen)

        JustInputView(screen)

        OptionTextDraw(attacktext, OPTIONFONT, battle_option_color[attack_color], OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y, screen)
        OptionTextDraw(skilltext, OPTIONFONT, battle_option_color[skill_color], OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + OPTIONSPACE, screen)
        OptionTextDraw('ぼうぎょ', OPTIONFONT, battle_option_color[diffence_color], OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + 2*OPTIONSPACE, screen)

        text_miko_HP = str(int(miko.hp))
        text_moribito_HP = str(int(moribito.hp))
        text_miko_MP = str(int(miko.mp))
        text_moribito_MP = str(int(moribito.mp))
        if miko.hp <= 0:
            text_miko_HP = str(int(0))
        if moribito.hp <= 0:
            text_moribito_HP = str(int(0))
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, GaugeView(miko), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, 200, 25), 3)
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, GaugeView(moribito), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, 200, 25), 3)
        OptionTextDraw('ルナ' + ' ' + text_miko_HP + ' ' + '/ ' + text_MIKO_MAXHP + '  ' + text_miko_MP , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y, screen)
        OptionTextDraw('シン' + ' ' + text_moribito_HP + ' ' + '/ ' + text_MORIBITO_MAXHP + '  ' + text_moribito_MP, OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y + OPTIONSPACE + 25, screen)

        # コマンド選択の処理
        for event in pygame.event.get():
            select_comand = 1
            if select_comand < 0:
                continue
            if event.type == KEYDOWN:
                if event.key == K_s:
                    SE.play()
                    if battle_option[battle_option_number] == 'attack':
                        battle_option_number = MAGIC
                        attack_color = OFF
                        skill_color = ON
                        diffence_color = OFF
                    elif battle_option[battle_option_number] == 'skill':
                        battle_option_number = DIFFENCE
                        attack_color = OFF
                        skill_color = OFF
                        diffence_color = ON
                    elif battle_option[battle_option_number] == 'diffence':
                        battle_option_number = DIFFENCE
                        attack_color = OFF
                        skill_color = OFF
                        diffence_color = ON
                elif event.key == K_w:
                    SE.play()
                    if battle_option[battle_option_number] == 'skill':
                        battle_option_number = ATTACK
                        attack_color = ON
                        skill_color = OFF
                        diffence_color = OFF
                    elif battle_option[battle_option_number] == 'diffence':
                        battle_option_number = MAGIC
                        attack_color = OFF
                        diffence_color = OFF
                        skill_color = ON
                    elif battle_option[battle_option_number] == 'attack':
                        battle_option_number = ATTACK
                        attack_color = ON
                        diffence_color = OFF
                        skill_color = OFF

                elif event.key == K_RETURN:
                    SE2.play()
                    skill_number = FinalSelectJudge(player, battle_option_number, screen)
                    if skill_number < 0:
                        select_comand = -1
                        continue
                    elif skill_number >= 0:
                        if CostCheck(player, skill_number) == True:
                            playermove[0] = player.number
                            playermove[1] = skill_number
                            playermove[2] = player.speed
                            return playermove
                        elif CostCheck(player, skill_number) == False:
                            pass

            elif event.type == QUIT:  
                battle_running = False
                terminate()

        if BATTLEQUIT == True:
            battle_running = False
            terminate()
                    
        pygame.display.update() 

        fpsclock.tick(FPS)

def SelectPlayerIcon(x, y, screen):
    screen.blit(icon, (x, y))

def StaffedRoll(stafflist, screen, fpsclock):
    staffroll_running = True
    staffrollquit = False
    y = [WINDOWHEIGHT / 2] * len(stafflist)
    space = 200
    speed = 5
    while staffroll_running:
        screen.blit(staffback, (0,0)) # スタッフロールの背景
        if staffrollquit == True:
            time.sleep(2)
            TextDraw("Press Enterkey", PRESSENTER, WHITE, WINDOWWIDTH / 2, 700, screen)

        for i in range(len(stafflist)):
            if (y[i] + i * space) > -80:
                text = STUFFEDROLL.render(stafflist[i], True, WHITE)
                textRect = text.get_rect()
                textRect.center = WINDOWWIDTH / 2, y[i] + i * space
                screen.blit(text, textRect)
            
        for j in range(len(stafflist)): # 文字の移動
            y[j] -= speed
            
        if (y[len(stafflist)-1] + (len(stafflist) - 1) * space) < -80:
            TextDraw("END", END, WHITE, WINDOWWIDTH / 2, WINDOWHEIGHT / 2, screen)
            staffrollquit = True

        pygame.display.update() 
        fpsclock.tick(FPS)

        if staffrollquit == True:
            staffroll_running = False
            time.sleep(1)

        for event in pygame.event.get():
                if event.type == QUIT:  
                    terminate()
    while True:
        TextDraw("Press Enter", PRESSENTER, WHITE, WINDOWWIDTH / 2 + 300, 700, screen)
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    terminate()

def BattleScreen(screen):
    screen.blit(battleback, (0, 0))
    if miko.hp > 0:
        screen.blit(battlemiko, (700, 300))
    elif miko.hp <= 0:
        screen.blit(diemiko, (700, 300))
    if moribito.hp > 0:
        screen.blit(battlemoribito, (700, 420))
    elif moribito.hp <= 0:
        screen.blit(diemoribito, (700, 420))
    screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))

    text_miko_HP = str(miko.hp)
    text_moribito_HP = str(moribito.hp)
    text_miko_MP = str(int(miko.mp))
    text_moribito_MP = str(int(moribito.mp))
    if miko.hp <= 0:
        text_miko_HP = str(int(0))
    if moribito.hp <= 0:
        text_moribito_HP = str(int(0))

    JustInputView(screen)

    screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
    screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))
    pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, GaugeView(miko), 25))
    pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, 200, 25), 3)
    pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, GaugeView(moribito), 25))
    pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, 200, 25), 3)
    OptionTextDraw('ルナ' + ' ' + text_miko_HP + ' ' + '/ ' + text_MIKO_MAXHP + '  ' + text_miko_MP  , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y, screen)
    OptionTextDraw('シン' + ' ' + text_moribito_HP + ' ' + '/ ' + text_MORIBITO_MAXHP + '  ' + text_moribito_MP , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y + OPTIONSPACE + 25, screen)

def StarEffect(screen, fpsclock):
    i = 0
    j = 0
    k = 0
    count = 0
    firstquit = False
    secondquit = True
    thirdquit = True
    SkillNameView("流星群！！", screen)
    STAR.play(1)
    while True:
        BattleScreen(screen)
        if firstquit == False:
            if i < len(stareffect):
                screen.blit(stareffect[i], (100,0))
                i += ANIMATIONSPEED

        if secondquit == False:
            if j < len(stareffect):
                screen.blit(stareffect[j], (150,50))
                j += ANIMATIONSPEED

        if thirdquit == False:
            if k < len(stareffect):
                screen.blit(stareffect[k], (250,25))
                k += ANIMATIONSPEED
                count += 1

        if i >= len(stareffect):
            i = 0
            firstquit = True
            secondquit = False
            thirdquit = True

        if j >= len(stareffect):
            j = 0
            firstquit = True
            secondquit = True
            thirdquit = False

        if k >= len(stareffect):
            k = 0
            firstquit = False
            secondquit = True
            thirdquit = True

        if count == 37:
            BattleScreen(screen)
            pygame.display.update()
            STAR.fadeout(1)
            return

        pygame.display.update() 
        fpsclock.tick(FPS)

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def SwordEffect(screen, fpsclock):
    i = 0
    SkillNameView("聖なる剣！！", screen)
    SWORD.play()
    while True:
        BattleScreen(screen)
        if i < len(swordeffect):
            screen.blit(swordeffect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED)

        if i >= len(swordeffect):
            BattleScreen(screen)
            pygame.display.update()
            SWORD.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def SlashEffect(screen, fpsclock):
    i = 0
    SkillNameView("壱ノ型！！", screen)
    SLASH1.play()
    while True:
        BattleScreen(screen)
        if i < len(slasheffect):
            screen.blit(slasheffect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED)

        if i >= len(slasheffect):
            BattleScreen(screen)
            pygame.display.update()
            SLASH1.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def Slash2Effect(screen, fpsclock):
    i = 0
    SkillNameView("弐ノ型！！", screen)
    SLASH2.play()
    while True:
        BattleScreen(screen)
        if i < len(slash2effect):
            screen.blit(slash2effect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED - 2)

        if i >= len(slash2effect):
            BattleScreen(screen)
            pygame.display.update()
            SLASH2.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def Slash3Effect(screen, fpsclock):
    i = 0
    SkillNameView("参ノ型！！", screen)
    SLASH1.play()
    while True:
        BattleScreen(screen)
        if i < len(slash3effect):
            screen.blit(slash3effect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED + 5)

        if i >= len(slash3effect):
            BattleScreen(screen)
            pygame.display.update()
            SLASH1.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def NormalSlashEffect(screen, fpsclock):
    i = 0
    SkillNameView("たたかう！！", screen)
    JustInput(moribito, screen, fpsclock)
    NORMALSLASH.play()
    while True:
        BattleScreen(screen)
        if i < len(normalslasheffect):
            screen.blit(normalslasheffect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED + 5)

        if i >= len(normalslasheffect):
            BattleScreen(screen)
            pygame.display.update()
            NORMALSLASH.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def NormalMagicEffect(screen, fpsclock):
    i = 0
    SkillNameView("たたかう！！", screen)
    JustInput(miko, screen, fpsclock)
    NORMALMAGIC.play()
    while True:
        BattleScreen(screen)
        JustInputView(screen)
        if i < len(normalmagiceffect):
            screen.blit(normalmagiceffect[i], (100,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED + 5)

        if i >= len(normalmagiceffect):
            BattleScreen(screen)
            pygame.display.update()
            NORMALMAGIC.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def BlackEffectToMiko(screen, fpsclock):
    i = 0
    SkillNameView("ルナへのこうげき", screen)
    JustInput(miko, screen, fpsclock)
    DARK.play()
    while True:
        BattleScreen(screen)
        if i < len(blackeffect):
            screen.blit(blackeffect[i], (500,0))
        i += 1

        pygame.display.update() 
        fpsclock.tick(20)

        if i >= len(blackeffect):
            BattleScreen(screen)
            pygame.display.update()
            DARK.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def BlackEffectToKishi(screen, fpsclock):
    i = 0
    SkillNameView("シンへのこうげき", screen)
    JustInput(moribito, screen, fpsclock)
    DARK.play()
    while True:
        BattleScreen(screen)
        if i < len(blackeffect):
            screen.blit(blackeffect[i], (500,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(20)

        if i >= len(blackeffect):
            BattleScreen(screen)
            pygame.display.update()
            DARK.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def MikoShieldEffect(screen, fpsclock):
    i = 0
    SkillNameView("ぼうぎょ！！", screen)
    SHIELD.play()
    while True:
        BattleScreen(screen)
        if i < len(shieldeffect):
            screen.blit(shieldeffect[i], (640,230))
        i += 1

        pygame.display.update() 
        fpsclock.tick(20)

        if i >= len(shieldeffect):
            BattleScreen(screen)
            pygame.display.update()
            SHIELD.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def KishiShieldEffect(screen, fpsclock):
    i = 0
    SkillNameView("ぼうぎょ！！", screen)
    SHIELD.play()
    while True:
        BattleScreen(screen)
        if i < len(shieldeffect):
            screen.blit(shieldeffect[i], (640,350))
        i += 1

        pygame.display.update() 
        fpsclock.tick(20)

        if i >= len(shieldeffect):
            BattleScreen(screen)
            pygame.display.update()
            SHIELD.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def CrowEffectToMiko(screen, fpsclock):
    i = 0
    j = 0
    crowquit = False
    SkillNameView("ルナへのこうげき", screen)
    JustInput(miko, screen, fpsclock)
    CROW.play()
    while True:
        BattleScreen(screen)
        if i < len(croweffect):
            screen.blit(croweffect[i], (560,100))
        i += 1

        if i >= len(croweffect):
            crowquit = True
            screen.blit(bloodeffect[j], (560,150))
            j += 1

        pygame.display.update() 
        if crowquit == False:
            fpsclock.tick(20)
        elif crowquit == True:
            fpsclock.tick(15)

        if j >= len(bloodeffect):
            BattleScreen(screen)
            pygame.display.update()
            CROW.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def CrowEffectToKishi(screen, fpsclock):
    i = 0
    j = 0
    crowquit = False
    SkillNameView("シンへのこうげき", screen)
    JustInput(moribito, screen, fpsclock)
    CROW.play()
    while True:
        BattleScreen(screen)
        if i < len(croweffect):
            screen.blit(croweffect[i], (560,200))
        i += 1

        if i >= len(croweffect):
            crowquit = True
            screen.blit(bloodeffect[j], (560,250))
            j += 1

        pygame.display.update() 
        if crowquit == False:
            fpsclock.tick(20)
        elif crowquit == True:
            fpsclock.tick(15)

        if j >= len(bloodeffect):
            BattleScreen(screen)
            pygame.display.update()
            CROW.fadeout(1)
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def LightEffectToMiko(screen, fpsclock):
    i = 0
    SkillNameView("ルナへのこうげき", screen)
    JustInput(miko, screen, fpsclock)
    LIGHT.play()
    while True:
        BattleScreen(screen)
        if i < len(lighteffect):
            screen.blit(lighteffect[i], (430,100))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED + 5)

        if i >= len(lighteffect):
            BattleScreen(screen)
            pygame.display.update()
            LIGHT.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def LightEffectToKishi(screen, fpsclock):
    i = 0
    SkillNameView("シンへのこうげき", screen)
    JustInput(moribito, screen, fpsclock)
    LIGHT.play()
    while True:
        BattleScreen(screen)
        if i < len(lighteffect):
            screen.blit(lighteffect[i], (430,230))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED + 5)

        if i >= len(lighteffect):
            BattleScreen(screen)
            pygame.display.update()
            LIGHT.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def HealEffect(screen, fpsclock):
    i = 0
    SkillNameView("癒しの光！！", screen)
    HEAL.play()
    while True:
        BattleScreen(screen)
        if i < len(healeffect):
            screen.blit(healeffect[i], (620,230))
            screen.blit(healeffect[i], (620,330))
        i += 1

        pygame.display.update() 
        fpsclock.tick(15)

        if i >= len(healeffect):
            BattleScreen(screen)
            pygame.display.update()
            HEAL.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def KishiSpecialEffect(screen, fpsclock):
    i = 0
    SkillNameView("おうぎ！！", screen)
    CutIn(kishicutin, screen, fpsclock)
    KISHISPECIAL.play()
    while True:
        screen.blit(battleback, (0, 0))
        if miko.hp > 0:
            screen.blit(battlemiko, (700, 300))
        elif miko.hp <= 0:
            screen.blit(diemiko, (700, 300))
        
        text_miko_HP = str(miko.hp)
        text_moribito_HP = str(moribito.hp)
        text_miko_MP = str(int(miko.mp))
        text_moribito_MP = str(int(moribito.mp))
        if miko.hp <= 0:
            text_miko_HP = str(int(0))
        if moribito.hp <= 0:
            text_moribito_HP = str(int(0))

        screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
        screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, GaugeView(miko), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, 200, 25), 3)
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, GaugeView(moribito), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, 200, 25), 3)
        OptionTextDraw('ルナ' + ' ' + text_miko_HP + ' ' + '/ ' + text_MIKO_MAXHP + '  ' + text_miko_MP  , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y, screen)
        OptionTextDraw('シン' + ' ' + text_moribito_HP + ' ' + '/ ' + text_MORIBITO_MAXHP + '  ' + text_moribito_MP , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y + OPTIONSPACE + 25, screen)
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,125))
        screen.blit(fade,(0,0))

        if moribito.hp > 0:
            screen.blit(battlemoribito, (700, 420))
        elif moribito.hp <= 0:
            screen.blit(diemoribito, (700, 420))
        screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))
        if i < len(kishispecialeffect):
            screen.blit(kishispecialeffect[i], (0,0))
        i += 1

        pygame.display.update() 
        fpsclock.tick(SLASHEFFECTSPEED)

        if i >= len(kishispecialeffect):
            BattleScreen(screen)
            pygame.display.update()
            KISHISPECIAL.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def MikoSpecialEffect(screen, fpsclock):
    i = 0
    SkillNameView("おうぎ！！", screen)
    CutIn(mikocutin, screen, fpsclock)
    MIKOSPECIAL.play(-1)
    while True:
        screen.blit(battleback, (0, 0))
        if miko.hp > 0:
            screen.blit(battlemiko, (700, 300))
        elif miko.hp <= 0:
            screen.blit(diemiko, (700, 300))
        
        text_miko_HP = str(miko.hp)
        text_moribito_HP = str(moribito.hp)
        text_miko_MP = str(int(miko.mp))
        text_moribito_MP = str(int(moribito.mp))
        if miko.hp <= 0:
            text_miko_HP = str(int(0))
        if moribito.hp <= 0:
            text_moribito_HP = str(int(0))

        screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
        screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, GaugeView(miko), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, 200, 25), 3)
        pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, GaugeView(moribito), 25))
        pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, 200, 25), 3)
        OptionTextDraw('ルナ' + ' ' + text_miko_HP + ' ' + '/ ' + text_MIKO_MAXHP + '  ' + text_miko_MP  , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y, screen)
        OptionTextDraw('シン' + ' ' + text_moribito_HP + ' ' + '/ ' + text_MORIBITO_MAXHP + '  ' + text_moribito_MP , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y + OPTIONSPACE + 25, screen)
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,125))
        screen.blit(fade,(0,0))

        if moribito.hp > 0:
            screen.blit(battlemoribito, (700, 420))
        elif moribito.hp <= 0:
            screen.blit(diemoribito, (700, 420))
        screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))
        if i < len(mikospecialeffect):
            screen.blit(mikospecialeffect[i], (0,0))
        i += 1

        pygame.display.update() 
        fpsclock.tick(12)

        if i >= len(mikospecialeffect):
            BattleScreen(screen)
            pygame.display.update()
            MIKOSPECIAL.fadeout(1)
            return 
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def SkillNameView(text, screen):
    skillname = True
    skillnamecount = 0
    while skillname:
        BattleScreen(screen)
        screen.blit(skillname_window, (150, 20))
        TextDraw(text, SKILLFONT, WHITE, 550, 100, screen)
        pygame.display.update()
        skillnamecount += 1
        if skillnamecount > 180:
            skillname = False
    return True

def EncountEffect(px, py, sisterX, sisterY, screen, fpsclock):
    i = 0
    ENCOUNT.play()
    while True:
        draw_basicmap(screen, basicmap)
        draw_adjustmap(screen, adjustmap)
        draw_eventmap(screen, eventmap)

        screen.blit(sister, (sisterX, sisterY))

        screen.blit(mikoAnime[1][1], (px, py))

        screen.blit(saintlight, (0,0))

        if i < len(encounteffect):
            screen.blit(encounteffect[i], (150,0))
        i += 1

        pygame.display.update() 
        fpsclock.tick(20)

        if i >= len(encounteffect):
            return 

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def CutIn(cutinimage, screen, fpsclock):
    alpha = 255
    CUTIN.play()
    while alpha > 0:
        BattleScreen(screen)
        screen.blit(cutinimage, (-100, 250))
        fade =pygame.Surface((355*3.5,45*3.5),flags=pygame.SRCALPHA)
        fade.fill((255,255,255,alpha))
        screen.blit(fade,(-100,250))
        
        pygame.display.update()
        alpha -= 10

        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

def GaugeView(player):
    return player.special / 500 * 200

def Heal(screen):
    healamount = 100
    miko.heal(healamount)
    moribito.heal(healamount)
    if miko.hp > 0:
        if miko.hp > MIKO_MAXHP:
            miko.hp = MIKO_MAXHP
    if moribito.hp > 0:
        if moribito.hp > MORIBITO_MAXHP:
            moribito.hp = MORIBITO_MAXHP
    miko.skillcost(MIKOSKILL3MP)
    BattleScreen(screen)
    strheal = str(int(healamount))
    healtext = HEALFONT.render(strheal, True, BLUE)
    screen.blit(healtext, (700, 230))
    screen.blit(healtext, (700, 350))
    pygame.display.update()

def Battle(allmove, screen, fpsclock):
    BattleScreen(screen)
    pygame.display.update()
    for move in allmove:
        if move[0] == -1:
            continue
        #SkillBox(move[1], screen, fpsclock)
        if move[0] == MIKO:
            if miko.hp > 0:
                SkillBox(move[1], screen, fpsclock)
                if (move[1] != 102) and (move[1] != 122) and (move[1] != -1): # 攻撃の処理
                    damage = Damage(miko, enemy, move[1])
                    DamageView(200, 200, damage, screen)
                    enemy.damage(damage)
                    if move[1] != 150:
                        miko.gaugeup(damage)
                    time.sleep(1)
                elif move[1] == 102: # 回復魔法の処理
                    Heal(screen)
                    time.sleep(1)
                elif move[1] == 122: # ぼうぎょの処理
                    time.sleep(1)
            elif miko.hp <= 0:
                pass

        elif move[0] == MORIBITO:
            SkillBox(move[1], screen, fpsclock)
            if moribito.hp > 0:
                if (move[1] != 222) and (move[1] != -1): # 攻撃の処理
                    damage = Damage(moribito, enemy, move[1])
                    DamageView(200, 200, damage, screen)
                    enemy.damage(damage)
                    if move[1] != 250:
                        moribito.gaugeup(damage)
                    time.sleep(1)
                elif move[1] == 222: # ぼうぎょの処理
                    time.sleep(1)
            elif moribito.hp <= 0:
                pass
        elif move[0] == ENEMY:
            SkillBox(move[1], screen, fpsclock)
            if move[1] % 2 == 0:
                if miko.diffencejudge == False:
                    damage = int(Damage(enemy, miko, move[1]))
                elif miko.diffencejudge == True:
                    damage = int(Damage(enemy, miko, move[1]) * 0.5)
                DamageView(720, 250, damage, screen)
                miko.damage(damage)
                time.sleep(1)
            elif move[1] % 2 == 1:
                #SkillBox(move[1], screen, fpsclock)
                if moribito.diffencejudge == False:
                    damage = int(Damage(enemy, moribito, move[1]))
                elif moribito.diffencejudge == True:
                    damage = int(Damage(enemy, moribito, move[1]) * 0.5)
                DamageView(720, 350, damage, screen)
                moribito.damage(damage)
                time.sleep(1)

        if WinJudge(miko, moribito, enemy):
            return True
        
    #time.sleep(1)

def SkillBox(number, screen, fpsclock):
    if number == 100:
        return StarEffect(screen, fpsclock)
    elif number == 101:
        return SwordEffect(screen, fpsclock)
    elif number == 102:
        return HealEffect(screen, fpsclock)
    elif number == 110:
        return NormalMagicEffect(screen, fpsclock)
    elif number == 122:
        return MikoShieldEffect(screen, fpsclock)
    elif number == 150:
        return MikoSpecialEffect(screen, fpsclock)
    elif number == 200:
        return SlashEffect(screen, fpsclock)
    elif number == 201:
        return Slash2Effect(screen, fpsclock)
    elif number == 202:
        return Slash3Effect(screen, fpsclock)
    elif number == 210:
        return NormalSlashEffect(screen, fpsclock)
    elif number == 222:
        return KishiShieldEffect(screen, fpsclock)
    elif number == 250:
        return KishiSpecialEffect(screen, fpsclock)
    elif number == 300:
        return BlackEffectToMiko(screen, fpsclock)
    elif number == 301:
        return BlackEffectToKishi(screen, fpsclock)
    elif number == 302:
        return CrowEffectToMiko(screen, fpsclock)
    elif number == 303:
        return CrowEffectToKishi(screen, fpsclock)
    elif number == 304:
        return LightEffectToMiko(screen, fpsclock)
    elif number == 305:
        return LightEffectToKishi(screen, fpsclock)
    
def WinJudge(player1, player2, enemy):
    if enemy.hp <= 0 or (player1.hp <= 0 and player2.hp <= 0):
        return True
    else:
        return False

def DamageView(x, y, damage, screen):
    BattleScreen(screen)
    strDamage = str(int(damage))
    damagetext = DAMAGEFONT.render(strDamage, True, WHITE)
    screen.blit(damagetext, (int(x), int(y)))
    pygame.display.update()

def DecisionOrder(allmove):
    allmove.sort(key = lambda x: x[2], reverse = True)
    return allmove

def CostCheck(player, skillnumber):
    if player.number == MIKO:
        if skillnumber == 0:
            if player.mp >= MIKOSKILL1MP:
                return True
            else:
                return False
        elif skillnumber == 1:
            if player.mp >= MIKOSKILL2MP:
                return True
            else:
                return False
        elif skillnumber == 2:
            if player.mp >= MIKOSKILL3MP:
                return True
            else:
                return False
        if skillnumber == 10:
            return True
        if skillnumber == 22:
            return True
        if skillnumber == 50:
            return True
            
    elif player.number == MORIBITO:
        if skillnumber == 0:
            if player.mp >= KISHISKILL1MP:
                return True
            else:
                return False
        elif skillnumber == 1:
            if player.mp >= KISHISKILL2MP:
                return True
            else:
                return False
        elif skillnumber == 2:
            if player.mp >= KISHISKILL3MP:
                return True
            else:
                return False
        if skillnumber == 10:
            return True
        if skillnumber == 22:
            return True
        if skillnumber == 50:
            return True

def FirstEvent(px, py, sisterX, sisterY, screen):
    # イベント処理
    i = 0
    #screen.blit(lines_window, (250, 10))
    pygame.display.update() 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    draw_basicmap(screen, basicmap)
                    draw_adjustmap(screen, adjustmap)
                    draw_eventmap(screen, eventmap)
                    screen.blit(sister, (sisterX, sisterY))
                    screen.blit(mikoAnime[1][1], (px, py))
                    screen.blit(saintlight, (0,0))
                    screen.blit(lines_window, (250, 10))
                    TextDraw(lineslist[i], LINESFONT, WHITE, 550, 110, screen)
                    pygame.display.update() 
                    i += 1
                if i >= len(lineslist):
                    return
                
def StoryRoll(storylist, back, screen, fpsclock):
    storyroll_running = True
    storyrollquit = False
    y = [WINDOWHEIGHT / 2] * len(storylist)
    space = 100
    speed = 3
    alpha = 0
    while storyroll_running:
        screen.blit(back, (0,0)) # スタッフロールの背景
        if storyrollquit == True:
            while alpha < 255:
                screen.blit(back, (0,0)) # スタッフロールの背景
                fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
                fade.fill((0,0,0,alpha))
                screen.blit(fade,(0,0))

                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == QUIT:  
                        terminate()
                
                alpha += 5

                fpsclock.tick(FPS)
            return
        for i in range(len(storylist)):
            if (y[i] + i * space) > -80:
                text = STORYROLL.render(storylist[i], True, BLACK)
                textRect = text.get_rect()
                textRect.center = WINDOWWIDTH / 2, y[i] + i * space
                screen.blit(text, textRect)
            
        for j in range(len(storylist)): # 文字の移動
            y[j] -= speed

        if (y[len(storylist)-1] + (len(storylist) - 1) * space) < -80:
            storyrollquit = True

        pygame.display.update() 
        fpsclock.tick(FPS)

        for event in pygame.event.get():
                if event.type == QUIT:  
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        storyrollquit = True

def PlayerWin(screen, fpsclock):
    count = 0
    effectquit = 0
    effect_running = True
    DEATH.play(-1)
    while effect_running:
        while count < 10:
            screen.blit(battleback, (0, 0))
            if miko.hp > 0:
                screen.blit(battlemiko, (700, 300))
            elif miko.hp <= 0:
                screen.blit(diemiko, (700, 300))
            if moribito.hp > 0:
                screen.blit(battlemoribito, (700, 420))
            elif moribito.hp <= 0:
                screen.blit(diemoribito, (700, 420))
            count += 1
            screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:  
                    pygame.mixer.music.stop() 
                    terminate()
            fpsclock.tick(FPS)
        
        while 10 <= count < 20:
            screen.blit(battleback, (0, 0))
            if miko.hp > 0:
                screen.blit(battlemiko, (700, 300))
            elif miko.hp <= 0:
                screen.blit(diemiko, (700, 300))
            if moribito.hp > 0:
                screen.blit(battlemoribito, (700, 420))
            elif moribito.hp <= 0:
                screen.blit(diemoribito, (700, 420))
            count += 1
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:  
                    pygame.mixer.music.stop() 
                    terminate()
            fpsclock.tick(FPS)
        effectquit += 1
        count = 0
        if effectquit == 3:
            DEATH.fadeout(1)
            return

def PlayerWinFadeOut(screen, fpsclock):
    alpha = 0
    while alpha < 255:
        screen.blit(battleback, (0, 0))
        if miko.hp > 0:
            screen.blit(battlemiko, (700, 300))
        elif miko.hp <= 0:
            screen.blit(diemiko, (700, 300))
        if moribito.hp > 0:
            screen.blit(battlemoribito, (700, 420))
        elif moribito.hp <= 0:
            screen.blit(diemoribito, (700, 420))
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha))
        screen.blit(fade,(0,0))
        pygame.display.update()
        alpha += 5

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

        fpsclock.tick(FPS)

def EnemyWinFadeOut(screen, fpsclock):
    alpha = 0
    while alpha < 255:
        screen.blit(battleback, (0, 0))
        if miko.hp > 0:
            screen.blit(battlemiko, (700, 300))
        elif miko.hp <= 0:
            screen.blit(diemiko, (700, 300))
        if moribito.hp > 0:
            screen.blit(battlemoribito, (700, 420))
        elif moribito.hp <= 0:
            screen.blit(diemoribito, (700, 420))
        screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha))
        screen.blit(fade,(0,0))
        pygame.display.update()
        alpha += 5

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

        fpsclock.tick(FPS)

def BattleLoop(screen, fpsclock):
    BATTLEBGM.play(-1)
    alpha = 255
    finalbattle = False
    finalbattlejudge = False
    while alpha > 0:
        BattleScreen(screen)
        fade =pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT),flags=pygame.SRCALPHA)
        fade.fill((0,0,0,alpha))
        screen.blit(fade,(0,0))
        pygame.display.update()
        alpha -= 5

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()

        fpsclock.tick(FPS)

    BattleTurtorial(screen, fpsclock)

    while True:
        i = 0
        if enemy.hp < 1000 and finalbattlejudge == False:
            finalbattlejudge = True
            finalbattle = True
        if enemy.hp < 1000 and finalbattle == True:
            enemy.attackchange(150)
            LASTBGM.play(-1)
            BATTLEBGM.fadeout(2)
            SkillNameView("敵の勢いが増した！！", screen)
            time.sleep(0.3)
            finalbattle = False
        enemyskillnumber = 0
        miko.diffencejudge = False
        moribito.diffencejudge = False
        allmove = [[],[],[]]
        for player in [miko, moribito]:
            if player.hp > 0:
                allmove[i] = PlayerMove(player, screen, fpsclock)
                if allmove[i][0] == MIKO:
                    allmove[i][1] += 100
                elif allmove[i][0] == MORIBITO:
                    allmove[i][1] += 200
            elif player.hp <= 0:
                allmove[i] = [-1, -1, -1]
            i += 1

        # ぼうぎょ選択時の処理
        if allmove[MIKO][1] == 122:
            miko.diffencejudge = True
            allmove[0][2] = 999
        if allmove[MORIBITO][1] == 222:
            moribito.diffencejudge = True
            allmove[1][2] = 999

        if miko.hp > 0 and moribito.hp > 0:
            enemyskillnumber = random.randint(0,5)
            allmove[2] = [ENEMY, ENEMYSKILL[enemyskillnumber], enemy.speed]
        elif miko.hp > 0:
            enemyskillnumber = random.randint(0,2)
            allmove[2] = [ENEMY, ENEMYSKILLTOMIKO[enemyskillnumber], enemy.speed]
        elif moribito.hp > 0:
            enemyskillnumber = random.randint(0,2)
            allmove[2] = [ENEMY, ENEMYSKILLTOMORIBITO[enemyskillnumber], enemy.speed]
        else: # バクで処理が終了するのを防いでいるため、ゲーム処理には関係ない
            allmove[2] =[-1, -1]
            break

        order = DecisionOrder(allmove)
       
        if Battle(order, screen, fpsclock):
            if miko.hp <= 0 and moribito.hp <= 0:
                LASTBGM.fadeout(2)
                EnemyWinFadeOut(screen, fpsclock)
                return False
            
            elif enemy.hp <= 0:
                LASTBGM.fadeout(2)
                PlayerWin(screen, fpsclock)
                PlayerWinFadeOut(screen, fpsclock)
                return True

        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.mixer.music.stop() 
                terminate()

def JustInputView(screen):
    fade =pygame.Surface((50,600),flags=pygame.SRCALPHA)
    fade.fill((0,0,0,125))
    screen.blit(fade,(1000,20))
    pygame.draw.rect(screen, WHITE, (1000, 20, 50, 600), 5)

def JustInput(player, screen, fpsclock):
    just = 0
    justquit = False
    while just <= 600:
        if justquit == True:
            break
        pygame.draw.rect(screen, YELLOW, (1000, 620 - just, 50, just))
        pygame.draw.rect(screen, WHITE, (1000, 20, 50, 600), 5)
        just += 30
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if just == 630:
                        JUST.play()
                        player.gaugeup(50)
                        time.sleep(0.3)
                        return
                    else:
                        return
        fpsclock.tick(FPS)

def Warnig(screen, fpsclock):
    while True:
        screen.fill(BLACK)
        TextDraw("注意", FONT, RED, WINDOWWIDTH / 2, 150, screen)
        TextDraw("この作品はフィクションです", STORYROLL, WHITE, WINDOWWIDTH / 2, 350, screen)
        TextDraw("実際の人物・団体・宗教とは", STORYROLL, WHITE, WINDOWWIDTH / 2, 450, screen)
        TextDraw("一切関係ありません", STORYROLL, WHITE, WINDOWWIDTH / 2, 550, screen)
        OptionTextDraw("Press Enter", PRESSENTER, WHITE, 800, 750, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    return
                
def ControlTurtorial(screen, fpsclock):
    while True:
        screen.fill(BLACK)
        TextDraw("あそび方", FONT, WHITE, WINDOWWIDTH / 2, 150, screen)
        screen.blit(wkey, (150,350))
        screen.blit(akey, (200,350))
        screen.blit(skey, (250,350))
        screen.blit(dkey, (300,350))
        OptionTextDraw("：押した方向に移動するぞ！", STORYROLL, WHITE, 350, 350, screen)
        screen.blit(enterkey, (250,450))
        OptionTextDraw("：決定するときに押そう！", STORYROLL, WHITE, 350, 450, screen)
        screen.blit(spacekey, (250,550))
        OptionTextDraw("：スキップしたいときに押そう！", STORYROLL, WHITE, 350, 550, screen)
        screen.blit(esckey, (250,650))
        OptionTextDraw("：戻りたいときに押そう！", STORYROLL, WHITE, 350, 650, screen)
        TextDraw("はじめに入力を半角に変えてね！", STORYROLL, WHITE, WINDOWWIDTH / 2, 270, screen)
        OptionTextDraw("Press Enter", PRESSENTER, WHITE, 800, 750, screen)

        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    return
                
def BattleTurtorialScreen1(screen):
    screen.blit(battleback, (0, 0))
    SelectPlayerIcon(725, 280, screen)
    screen.blit(battlemiko, (700, 300))
    screen.blit(battlemoribito, (700, 420))
    screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))

    text_miko_HP = str(miko.hp)
    text_moribito_HP = str(moribito.hp)
    text_miko_MP = str(int(miko.mp))
    text_moribito_MP = str(int(moribito.mp))

    JustInputView(screen)

    screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
    screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))
    pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, GaugeView(miko), 25))
    pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 75, 200, 25), 3)
    pygame.draw.rect(screen, YELLOW, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, GaugeView(moribito), 25))
    pygame.draw.rect(screen, WHITE, (STATUS_WINDOW_X + ADJUST_X + 75, STATUS_WINDOW_Y + ADJUST_Y + 150, 200, 25), 3)
    OptionTextDraw('たたかう', OPTIONFONT, YELLOW, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y, screen)
    OptionTextDraw('まほう', OPTIONFONT, WHITE, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + OPTIONSPACE, screen)
    OptionTextDraw('ぼうぎょ', OPTIONFONT, WHITE, OPTION_X + ADJUST_X, OPTION_Y + ADJUST_Y + 2*OPTIONSPACE, screen)
    OptionTextDraw('ルナ' + ' ' + text_miko_HP + ' ' + '/ ' + text_MIKO_MAXHP + '  ' + text_miko_MP  , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y, screen)
    OptionTextDraw('シン' + ' ' + text_moribito_HP + ' ' + '/ ' + text_MORIBITO_MAXHP + '  ' + text_moribito_MP , OPTIONFONT, WHITE, PLAYER_STATUS_X + ADJUST_X, PLAYER_STATUS_Y + ADJUST_Y + OPTIONSPACE + 25, screen)

    for event in pygame.event.get():
        if event.type == QUIT:  
            terminate()

def BattleTurtorialScreen2(screen):
    screen.blit(battleback, (0, 0))
    SelectPlayerIcon(725, 280, screen)
    screen.blit(battlemiko, (700, 300))
    screen.blit(battlemoribito, (700, 420))
    screen.blit(BossEnemy[1][0], (BossEnemy[1][1], BossEnemy[1][2]))

    JustInputView(screen)

    screen.blit(status_window, (STATUS_WINDOW_X + ADJUST_X, STATUS_WINDOW_Y + ADJUST_Y))
    screen.blit(comand_window, (COMAND_WINDOW_X + ADJUST_X, COMAND_WINDOW_Y + ADJUST_Y))
    OptionTextDraw('流星群　　　中　　20', OPTIONFONT, YELLOW, SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y, screen)
    OptionTextDraw('聖なる剣　　大　　30', OPTIONFONT, WHITE, SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + OPTIONSPACE, screen)
    OptionTextDraw('癒しの光　　癒　　35', OPTIONFONT, WHITE, SKILL_X + ADJUST_X, SKILL_Y + ADJUST_Y + 2*OPTIONSPACE, screen)


    for event in pygame.event.get():
        if event.type == QUIT:  
            terminate()

def BattleTurtorial(screen, fpsclock):
    TURTORIALDECISION = False
    TURTORIAL_OPTION_COLOR = [WHITE, YELLOW] 
    START_NUMBER = 1
    QUIT_NUMBER = 0
    NOWACTION = 1
    NOTNOWACTION = 0
    DecisionTurtorial(decisionturtoriallist, screen, fpsclock)
    while True:
        BattleTurtorialScreen1(screen)
        screen.blit(lines_window, (250, 10))
        TextDraw("はい", LINESFONT, TURTORIAL_OPTION_COLOR[START_NUMBER], 500, 110, screen)
        TextDraw("いいえ", LINESFONT, TURTORIAL_OPTION_COLOR[QUIT_NUMBER], 600, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        if TURTORIALDECISION == True:
            break

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    SE.play()
                    if START_NUMBER == NOWACTION:
                        START_NUMBER = NOTNOWACTION
                        QUIT_NUMBER = NOWACTION
                if event.key == K_a:
                    SE.play()
                    if START_NUMBER == NOTNOWACTION:
                        START_NUMBER = NOWACTION
                        QUIT_NUMBER = NOTNOWACTION
                if event.key == K_RETURN:
                    SE2.play()
                    if START_NUMBER == NOTNOWACTION:
                        return
                    elif START_NUMBER == NOWACTION:
                        TURTORIALDECISION = True
        
    PlayerTurtorial(playerturtoriallist, screen, fpsclock)
    StatusTurtorial(statusturtoriallist, screen, fpsclock)
    ComandTurtorial(comandturtoriallist, screen, fpsclock)
    SkillTurtorial(skillturtoriallist, screen, fpsclock)
    JustGaugeTurtorial(justgaugeturtoriallist, screen, fpsclock)
    return

def PlayerTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
            return
        BattleTurtorialScreen1(screen)
        pygame.draw.rect(screen, RED, turtorialhighlightlist[0], 7)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

def ComandTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
           return
        BattleTurtorialScreen1(screen)
        pygame.draw.rect(screen, RED, turtorialhighlightlist[2], 7)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

def SkillTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
           return
        BattleTurtorialScreen2(screen)
        pygame.draw.rect(screen, RED, turtorialhighlightlist[3], 7)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

def StatusTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
           return
        BattleTurtorialScreen1(screen)
        pygame.draw.rect(screen, RED, turtorialhighlightlist[3], 7)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

def JustGaugeTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
           return
        BattleTurtorialScreen1(screen)
        pygame.draw.rect(screen, RED, turtorialhighlightlist[1], 7)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

def DecisionTurtorial(list, screen, fpsclock):
    i = 0
    while True:
        if i >= len(list):
           return
        BattleTurtorialScreen1(screen)
        screen.blit(lines_window, (250, 10))
        TextDraw(list[i], LINESFONT, WHITE, 550, 110, screen)
        pygame.display.update()
        fpsclock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:  
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    SE2.play()
                    i = i + 1

if __name__ == '__main__':
    main()

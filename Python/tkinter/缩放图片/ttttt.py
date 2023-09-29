import random
import sys
import time

import pygame

# 地雷数量
MINE_COUNT = 99
# 每个方格的大小（宽、高都为20）
SIZE = 20
# 方格的行数
BLOCK_ROW_NUM = 16
# 方格的列数
BLOCK_COL_NUM = 30
# 游戏窗口的宽、高
SCREEN_WIDTH, SCREEN_HEIGHT = BLOCK_COL_NUM * SIZE, (BLOCK_ROW_NUM + 2) * SIZE


def get_mine_flag_num(board_list):
    """
    计算还剩多少颗雷
    """
    num = 0
    for line in board_list:
        for num_dict in line:
            if num_dict.get("closed_num") == "雷标记":
                num += 1

    return num


def open_all_mine(board_list):
    """
    显示所有的雷
    """
    for row, line in enumerate(board_list):
        for col, num_dict in enumerate(line):
            if num_dict.get("opened_num") == "雷":
                num_dict["opened"] = True


def get_mine_num(row, col, board_list):
    """
    计算点击的空格周围的雷的数量
    """
    # 生成起始位置、终止位置
    row_start = row - 1 if row - 1 >= 0 else row
    row_stop = row + 2 if row + 1 <= BLOCK_ROW_NUM - 1 else row + 1
    col_start = col - 1 if col - 1 >= 0 else col
    col_stop = col + 2 if col + 1 <= BLOCK_COL_NUM - 1 else col + 1

    # 循环遍历当前方格周围的雷的数量
    mine_num = 0
    for i in range(row_start, row_stop):
        for j in range(col_start, col_stop):
            if board_list[i][j].get("opened_num") == "雷":
                mine_num += 1
    return mine_num


def set_nums_blank(row, col, board_list):
    """
    判断当前位置的周边位置是否为空，如果是则继续判断，
    最终能够实现点击一个空位置后连续的空位置都能够显示出来
    """
    mine_num = get_mine_num(row, col, board_list)
    print("row=%d, col=%d, mine_num=%d" % (row, col, mine_num))
    if mine_num == 0:
        board_list[row][col]['opened'] = True
        board_list[row][col]["opened_num"] = 0
        board_list[row][col]["closed_num"] = "空"
        # 判断对角是否是数字
        for i, j in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
            if 0 <= row + i <= 15 and 0 <= col + j <= 29:
                mine_num = get_mine_num(row + i, col + j, board_list)
                if mine_num:
                    board_list[row + i][col + j]['opened'] = True
                    board_list[row + i][col + j]["opened_num"] = mine_num
                    board_list[row + i][col + j]["closed_num"] = "空"

        # 判断剩下4个位置是否是也是0，即空
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= row + i <= 15 and 0 <= col + j <= 29:
                if not board_list[row + i][col + j].get("opened"):
                    set_nums_blank(row + i, col + j, board_list)
    else:
        board_list[row][col]['opened'] = True
        board_list[row][col]["opened_num"] = mine_num
        board_list[row][col]["closed_num"] = "空"


def left_click_block(row, col, board_list):
    """
    左击空格后的处理
    """
    if board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") != "雷":
        # 如果不是雷，那么就计算当前位置数字
        mine_num = get_mine_num(row, col, board_list)
        print("地雷数:", mine_num)
        board_list[row][col]["opened_num"] = mine_num
        board_list[row][col]["opened"] = True  # 标记为"打开"状态
        board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误
        if mine_num == 0:
            # 如果方格周边没有雷此时，判断是否有连续空位置
            set_nums_blank(row, col, board_list)
    elif board_list[row][col].get("opened") is False and board_list[row][col].get("opened_num") == "雷":
        board_list[row][col]["opened_num"] = "踩雷"  # 标记为"踩雷"图片
        board_list[row][col]["opened"] = True  # 标记为"打开"状态
        board_list[row][col]["closed_num"] = "空"  # 标记为"未打开时的状态为空格"，防止显示剩余雷数错误
        return True


def create_random_board(row, col, mine_num):
    """
    得到一个随机的棋盘
    """
    # 随机布雷
    nums = [{"opened": False, "opened_num": 0, 'closed_num': "空"} for _ in range(row * col - mine_num)]  # 16x30-99 表示的是生成381个0
    nums += [{"opened": False, "opened_num": "雷", 'closed_num': "空"} for _ in range(mine_num)]  # 99颗地雷
    random.shuffle(nums)  # 乱序，此时nums是乱的
    return [list(x) for x in zip(*[iter(nums)] * col)]


def right_click_block(row, col, board_list):
    """
    右击方格后更新其状态（标记为雷、问号?、取消标记）
    """
    if board_list[row][col].get("opened") is False:
        if board_list[row][col]["closed_num"] == "空":
            board_list[row][col]["closed_num"] = "雷标记"
        elif board_list[row][col]["closed_num"] == "雷标记":
            board_list[row][col]["closed_num"] = "疑问标记"
        elif board_list[row][col]["closed_num"] == "疑问标记":
            board_list[row][col]["closed_num"] = "空"


def click_block(x, y, board_list):
    """
    检测点击的是哪个方格（即第x行，第y列）
    """
    # 计算出点击的空格的行、列
    for row, line in enumerate(board_list):
        for col, _ in enumerate(line):
            if col * SIZE <= x <= (col + 1) * SIZE and (row + 2) * SIZE <= y <= (row + 2 + 1) * SIZE:
                print("点击的空格的位置是:", row, col)
                return row, col


def run(screen):
    bgcolor = (225, 225, 225)  # 背景色

    # 要显示的棋盘
    # board_list = [[0] * BLOCK_COL_NUM for _ in range(BLOCK_ROW_NUM)]
    board_list = create_random_board(BLOCK_ROW_NUM, BLOCK_COL_NUM, MINE_COUNT)  # 16行、30列，有99颗地雷

    # 默认的方格图片
    img_blank = pygame.image.load('/tkinter/缩放图片/closed.png').convert()
    img_blank = pygame.transform.smoothscale(img_blank, (SIZE, SIZE))
    # "雷标记"图片
    img_mine_flag = pygame.image.load('/tkinter/缩放图片/flag.png').convert()
    img_mine_flag = pygame.transform.smoothscale(img_mine_flag, (SIZE, SIZE))
    # "雷"图片
    img_mine = pygame.image.load('/tkinter/缩放图片/mine.png').convert()
    img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))
    # "疑问标记"图片
    img_ask = pygame.image.load('/tkinter/缩放图片/mine_red.png').convert()
    img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))
    # "踩雷"图片
    img_blood = pygame.image.load('/tkinter/缩放图片/mine_red.png').convert()
    img_blood = pygame.transform.smoothscale(img_blood, (SIZE, SIZE))
    # "表情"图片
    face_size = int(SIZE * 1.25)
    img_face_fail = pygame.image.load('/tkinter/缩放图片/type0.png').convert()
    img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
    img_face_normal = pygame.image.load('/tkinter/缩放图片/type0.png').convert()
    img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
    img_face_success = pygame.image.load('/tkinter/缩放图片/type0.png').convert()
    img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
    # "表情"位置
    face_pos_x = (SCREEN_WIDTH - face_size) // 2
    face_pos_y = (SIZE * 2 - face_size) // 2
    # 类的数量图片
    img0 = pygame.image.load('/tkinter/缩放图片/type0.png').convert()
    img0 = pygame.transform.smoothscale(img0, (SIZE, SIZE))
    img1 = pygame.image.load('/tkinter/缩放图片/type1.png').convert()
    img1 = pygame.transform.smoothscale(img1, (SIZE, SIZE))
    img2 = pygame.image.load('/tkinter/缩放图片/type2.png').convert()
    img2 = pygame.transform.smoothscale(img2, (SIZE, SIZE))
    img3 = pygame.image.load('/tkinter/缩放图片/type3.png').convert()
    img3 = pygame.transform.smoothscale(img3, (SIZE, SIZE))
    img4 = pygame.image.load('/tkinter/缩放图片/type4.png').convert()
    img4 = pygame.transform.smoothscale(img4, (SIZE, SIZE))
    img5 = pygame.image.load('/tkinter/缩放图片/type5.png').convert()
    img5 = pygame.transform.smoothscale(img5, (SIZE, SIZE))
    img6 = pygame.image.load('/tkinter/缩放图片/type6.png').convert()
    img6 = pygame.transform.smoothscale(img6, (SIZE, SIZE))
    img7 = pygame.image.load('/tkinter/缩放图片/type7.png').convert()
    img7 = pygame.transform.smoothscale(img7, (SIZE, SIZE))
    img8 = pygame.image.load('/tkinter/缩放图片/type8.png').convert()
    img8 = pygame.transform.smoothscale(img8, (SIZE, SIZE))
    img_dict = {
        0: img0,
        1: img1,
        2: img2,
        3: img3,
        4: img4,
        5: img5,
        6: img6,
        7: img7,
        8: img8,
        '雷标记': img_mine_flag,
        '雷': img_mine,
        '空': img_blank,
        '疑问标记': img_ask,
        '踩雷': img_blood,
    }
    # 标记是否踩到雷
    game_over = False
    # 游戏状态
    game_status = "normal"
    # 显示雷的数量、耗时用到的资源
    font = pygame.font.Font('/Users/mac/PycharmProjects/pythonProject1/tkinter/缩放图片/resource-1.ttf', SIZE * 2)  # 字体
    f_width, f_height = font.size('999')
    red = (200, 40, 40)
    # 标记出雷的个数
    flag_count = 0
    # 记录耗时
    elapsed_time = 0
    last_time = time.time()
    start_record_time = False

    # 创建计时器（防止while循环过快，占用太多CPU的问题）
    clock = pygame.time.Clock()
    while True:
        # 事件检测（鼠标点击、键盘按下等）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button:
                b1, b2, b3 = pygame.mouse.get_pressed()
                mouse_click_type = None
                if b1 and not b2 and not b3:  # 左击
                    mouse_click_type = "left"
                elif not b1 and not b2 and b3:  # 右击
                    mouse_click_type = "right"
                print("点击了鼠标的[%s]键" % mouse_click_type)
                x, y = pygame.mouse.get_pos()
                if game_status == "normal" and 2 * SIZE <= y <= SCREEN_HEIGHT:
                    # 计算点击的是哪个空
                    position = click_block(x, y, board_list)
                    if position:
                        if mouse_click_type == "right":
                            # 如果右击方格，那么就更新其状态
                            right_click_block(*position, board_list)
                            # 更新标记的雷的数量
                            flag_count = get_mine_flag_num(board_list)
                            start_record_time = True  # 开始记录耗时
                        elif mouse_click_type == "left":
                            # 点击空格的处理
                            game_over = left_click_block(*position, board_list)
                            print("是否踩到雷", game_over)
                            start_record_time = True  # 开始记录耗时
                            # 更新标记的雷的数量
                            flag_count = get_mine_flag_num(board_list)
                            if game_over:
                                # 将所有雷的位置，标记出来
                                open_all_mine(board_list)
                                # 更改游戏状态
                                game_status = "fail"
                                # 停止记录耗时
                                start_record_time = False
                elif face_pos_x <= x <= face_pos_x + face_size and face_pos_y <= y <= face_pos_y + face_size:
                    # 重来一局
                    print("点击了再来一局...")
                    return

        # 填充背景色
        screen.fill(bgcolor)

        # 显示方格
        for i, line in enumerate(board_list):
            for j, num_dict in enumerate(line):
                if num_dict.get("opened"):
                    screen.blit(img_dict[num_dict.get("opened_num")], (j * SIZE, (i + 2) * SIZE))
                else:
                    screen.blit(img_dict[num_dict.get("closed_num")], (j * SIZE, (i + 2) * SIZE))

        # 显示表情
        if game_status == "win":
            screen.blit(img_face_success, (face_pos_x, face_pos_y))
        elif game_status == "fail":
            screen.blit(img_face_fail, (face_pos_x, face_pos_y))
        else:
            screen.blit(img_face_normal, (face_pos_x, face_pos_y))

        # 显示剩余雷的数量
        mine_text = font.render('%02d' % (MINE_COUNT - flag_count), True, red)
        screen.blit(mine_text, (30, (SIZE * 2 - f_height) // 2 - 2))

        # 显示耗时
        if start_record_time and time.time() - last_time >= 1:
            elapsed_time += 1
            last_time = time.time()
        mine_text = font.render('%03d' % elapsed_time, True, red)
        screen.blit(mine_text, (SCREEN_WIDTH - f_width - 30, (SIZE * 2 - f_height) // 2 - 2))

        # 刷新显示（此时窗口才会真正的显示）
        pygame.display.update()
        # FPS（每秒钟显示画面的次数）
        clock.tick(60)  # 通过一定的延时，实现1秒钟能够循环60次


def main():
    """
    循环调用run函数，每调用一次就重新来一局游戏
    """
    pygame.init()
    pygame.display.set_caption('扫雷')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        run(screen)


if __name__ == '__main__':
    main()
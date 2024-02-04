import beijing_life as bl
import sys

bl.start_game()
# 读取游戏状态和市场价格
user_state, market_prices, game_message = bl.get_state()

print(user_state, market_prices, game_message)

# 购买 20 个盗版 VCD, 游戏
bl.buy_goods("CD", 40)
# 移动到东直门
bl.move("东直门")

# 读取游戏状态和市场价格
user_state, market_prices, game_message = bl.get_state()

print(user_state, market_prices, game_message)

# 卖出 20 个盗版 VCD, 游戏
bl.sell_goods("CD", 30)
# 买进 10 个伪劣化妆品
bl.buy_goods("COSMETIC", 10)
# 还债 1000 元
bl.repay_debt(1000)
# 移动到东直门
bl.move("东直门")

# 读取游戏状态和市场价格
user_state, market_prices, game_message = bl.get_state()

print(user_state, market_prices, game_message)

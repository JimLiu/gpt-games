import random

# Goods Configuration
Goods = {
    "COSMETIC": "伪劣化妆品",
    "CIGARETTE": "进口香烟",
    "CAR": "进口汽车",
    "PHONES": "水货手机",
    "ALCOHOL": "假白酒",
    "BABY": "上海小宝贝 18 禁",
    "CD": "盗版 VCD, 游戏",
    "TOY": "进口玩具",
}

# Debt Rate
debt_rate = 0.1

# Max Capacity
max_capacity = 100

# Prices Configuration
prices_config = {
    "CIGARETTE": {"min": 10, "base": 100, "max": 450},
    "BABY": {"min": 1000, "base": 5000, "max": 14000},
    "CD": {"min": 5, "base": 10, "max": 100},
    "ALCOHOL": {"min": 100, "base": 1000, "max": 3500},
    "COSMETIC": {"min": 10, "base": 65, "max": 300},
    "CAR": {"min": 5000, "base": 15000, "max": 30000},
    "PHONES": {"min": 500, "base": 750, "max": 1500},
    "TOY": {"min": 100, "base": 250, "max": 850},
}

# Market Prices (Initial Values)
market_prices = {
    "CIGARETTE": 200,
    "BABY": 7500,
    "CD": 50,
    "ALCOHOL": 1500,
    "COSMETIC": 500,
    "CAR": 20000,
    "PHONES": 1000,
    "TOY": 400,
}

# User State
user_state = {
    "location": "北京站",
    "cash": 2000,
    "debt": 5000,
    "goods": [],
    "daysLeft": 20,
    "totalGoods": 0,
    "currentEvent": None
}

# Locations
locations = [
    "西直门", "积水潭", "东直门", "苹果园", "公主坟", "复兴门", "建国门", "长椿街",
    "崇文门", "北京站", "海淀大街", "亚运村", "三元西桥", "八角西路", "翠微路", "府右街",
    "永安里", "玉泉营", "永定门", "方庄"
]

# Events Configuration
events = [
    {"description": "《北京真理报》社论：“提倡爱美，落到实处”，伪劣化妆品大受欢迎！",
        "type": "price", "goods": "COSMETIC", "rate": 4},
    {"description": "谢不疯在晚会上说：“我酷！我使用伪劣化妆品！”，伪劣化妆品供不应求！",
        "type": "price", "goods": "COSMETIC", "rate": 7},
    {"description": "《北京经济小报》社论：“走私汽车大力推进汽车消费！”",
        "type": "price", "goods": "CAR", "rate": 3},
    {"description": "北京的孩子们都忙于上网学习，进口玩具没人愿意买。",
        "type": "price", "goods": "TOY", "rate": 1 / 7},
    {"description": "市场上充斥着来自福建的走私香烟", "type": "price",
        "goods": "CIGARETTE", "rate": 1 / 7},
    {"description": "俺老乡回家前把一些山西假白酒给俺！", "type": "goods",
        "goods": "ALCOHOL", "quantity": 7},
    {"description": "厦门的老同学资助俺几辆走私汽车。",
        "type": "goods", "goods": "CAR", "quantity": 2},
    {"description": "工商局扫荡后，俺在黑暗角落里发现了老乡丢失的进口香烟。",
        "type": "goods", "goods": "CIGARETTE", "quantity": 6},
    {"description": "日本产品又出事故！日本人死不认账，拒绝赔偿！村长把他的水货手机用高价强卖给俺。",
        "type": "goods", "goods": "PHONES", "quantity": 3, "debt": 5000},
    {"description": "专家提议提高大学生“动手素质”, 进口玩具大受欢迎。",
        "type": "price", "goods": "TOY", "rate": 2},
    {"description": "有人说：生病不用打针吃药，喝假白酒（剧毒）就可以！",
        "type": "price", "goods": "ALCOHOL", "rate": 3},
    {"description": "医院的秘密报告：“《上海小宝贝》功效甚过伟哥”!",
        "type": "price", "goods": "BABY", "rate": 4},
    {"description": "文盲说：“2000 年诺贝尔文学奖？呸！不如盗版 VCD 港台片。",
        "type": "price", "goods": "CD", "rate": 4},
    {"description": "北京的富人疯狂地购买走私汽车！", "type": "price", "goods": "CAR", "rate": 7},
    {"description": "俺怜悯扮演成乞丐的老太太们。（损失 10% 现金）", "type": "cash", "rate": 0.9},
    {"description": "一个汉子在街头拦住俺：“哥们，给点钱用！”（损失 10% 现金）", "type": "cash", "rate": 0.9},
    {"description": "一个大个子碰了俺一下，说：“别挤了！”（损失 40% 现金）", "type": "cash", "rate": 0.6},
    {"description": "三个带红袖章的老太太揪住俺：“你是外地人？罚款！”（损失 20% 现金）",
        "type": "cash", "rate": 0.8},
    {"description": "两个猛男揪住俺：“交市话费、长话附加费、上网费。”（损失 15% 现金）",
        "type": "cash", "rate": 0.85},
    {"description": "副主任严肃地说：“晚上别来我家给我送钱。”（损失 10% 现金）", "type": "cash", "rate": 0.9},
    {"description": "北京空气污染得厉害，俺去氧吧吸氧..（损失 5% 现金）", "type": "cash", "rate": 0.95},
]


# 这里只包含了一个示例事件，您需要根据游戏的设计添加更多事件


def process_next_day(location):
    # Step 1: Update days left
    user_state['daysLeft'] -= 1

    # Step 2: Update debt
    user_state['debt'] *= (1 + debt_rate)

    # Step 3: Update market prices
    for good, config in prices_config.items():
        market_prices[good] = random.randint(config['min'], config['max'])

    # Step 4: Check if days left is 0
    if user_state['daysLeft'] == 0:
        # Sell all goods
        total_value = sum(
            market_prices[item['type']] * item['quantity'] for item in user_state['goods'])
        user_state['cash'] += total_value
        user_state['goods'] = []

        return

    # Step 5: Generate a random event
    event = random.choice(events)
    user_state['currentEvent'] = event['description']
    process_event(event)

    return event


def process_event(event):
    # Check for debt in the event and update if exists
    if 'debt' in event:
        user_state['debt'] += event['debt']

    # Process based on event type
    if event['type'] == 'price':
        # Update the price of the goods
        market_prices[event['goods']] *= event['rate']
    elif event['type'] == 'goods':
        # Check if the goods already exist in user's goods
        existing_item = next(
            (item for item in user_state['goods'] if item['type'] == event['goods']), None)
        if existing_item:
            # Update quantity if item already exists
            existing_item['quantity'] += event['quantity']
        else:
            # Add new item if it doesn't exist
            user_state['goods'].append(
                {'type': event['goods'], 'quantity': event['quantity']})
    elif event['type'] == 'cash':
        # Update the user's cash
        user_state['cash'] *= event['rate']


def sell_goods(goods, quantity):
    # Find the item in user's inventory
    item = next((i for i in user_state['goods'] if i['type'] == goods), None)

    # If item does not exist or quantity is zero, do nothing
    if not item or item['quantity'] == 0:
        return

    # Calculate actual quantity to sell
    actual_quantity = min(item['quantity'], quantity)

    # Calculate total sale price and update cash
    sale_price = actual_quantity * market_prices[goods]
    user_state['cash'] += sale_price

    # Update the item quantity
    item['quantity'] -= actual_quantity
    if item['quantity'] == 0:
        user_state['goods'].remove(item)

    # Update current capacity
    user_state['totalGoods'] -= actual_quantity


def buy_goods(goods, quantity):
    # Calculate the maximum quantity that can be bought
    available_capacity = max_capacity - user_state['totalGoods']
    max_affordable_quantity = user_state['cash'] // market_prices[goods]
    actual_quantity = min(quantity, available_capacity,
                          max_affordable_quantity)

    # If no quantity can be bought, do nothing
    if actual_quantity <= 0:
        return

    # Calculate total purchase price and update cash
    purchase_price = actual_quantity * market_prices[goods]
    user_state['cash'] -= purchase_price

    # Update the item in inventory
    existing_item = next(
        (item for item in user_state['goods'] if item['type'] == goods), None)
    if existing_item:
        existing_item['quantity'] += actual_quantity
    else:
        user_state['goods'].append(
            {'type': goods, 'quantity': actual_quantity})

    # Update current capacity
    user_state['totalGoods'] += actual_quantity


def generate_game_info():

    # Gather user state information
    location = user_state['location']
    cash = user_state['cash']
    debt = user_state['debt']
    days_left = user_state['daysLeft']

    # Format the items information
    goods_info = "\n".join(
        [f"- {Goods[item['type']]}：{item['quantity']}件" for item in user_state['goods']]) if user_state['goods'] else "无"

    # Format the market prices
    market_prices_info = "\n".join(
        [f"- {Goods[good]}：{price}元" for good, price in market_prices.items()])

    # Combine all information into a Markdown formatted text
    game_info = f"""当前事件：{user_state['currentEvent']}
当前位置：{location}
现金：{cash} 元
负债：{debt} 元
剩余天数：{days_left}天

拥有的物品：
{goods_info}

市场价格：
{market_prices_info}
"""
    return game_info


def get_state():
    # Copy user_state to avoid mutating the original
    state = user_state.copy()

    # Replace item types with their real names in user's items
    state['goods'] = [{'type': Goods[item['type']],
                       'quantity': item['quantity']} for item in state['goods']]

    # Replace market_prices keys with their real names
    prices = {Goods[good]: price for good, price in market_prices.items()}

    game_message = generate_game_info()

    return user_state, market_prices, game_message


def move(location=None):
    # Check if the location is valid or not provided
    if location not in locations or not location:
        location = random.choice(
            [loc for loc in locations if loc != user_state['location']])

    # Update the user's location
    user_state['location'] = location

    # Process the next day
    process_next_day(location)

    # Return user status and current event
    return get_state()


def start_game():
    # Reset user state
    user_state['location'] = "北京站"
    user_state['cash'] = 2000
    user_state['debt'] = 5000
    user_state['goods'] = []
    user_state['daysLeft'] = 20
    user_state['totalGoods'] = 0
    user_state['currentEvent'] = None

    # Reset market prices
    for good, config in prices_config.items():
        market_prices[good] = random.randint(config['min'], config['max'])

    # Return user status and current event
    return get_state()


def repay_debt(amount):
    # Calculate the maximum amount that can be repaid, which is the lesser of half the cash or the debt
    max_repayable = min(user_state['cash'] / 2, user_state['debt'])

    # Calculate the actual repayment amount
    actual_repayment = min(amount, max_repayable)

    # Update the cash and debt in user_state
    user_state['cash'] -= actual_repayment
    user_state['debt'] -= actual_repayment

    # Ensure values do not go negative
    user_state['cash'] = max(0, user_state['cash'])
    user_state['debt'] = max(0, user_state['debt'])

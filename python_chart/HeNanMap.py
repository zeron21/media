import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

# 数据准备
data = {
    '郑州市': 248,
    '信阳市': -242,
    '周口市': -300,
    '驻马店市': -216,
    '南阳市': -199,
    '三门峡市': -4,
    '洛阳市': -25,
    '平顶山市': -52,
    '漯河市': -18,
    '许昌市': -54,
    '济源市': 1,
    '焦作市': -18,
    '开封市': -70,
    '商丘市': -197,
    '新乡市': -39,
    '鹤壁市': -3,
    '安阳市': -75,
    '濮阳市': -40
}
df = pd.DataFrame({'city': list(data.keys()), 'value': list(data.values())})

# 绘制地图
map_chart = (
    Map()
    .add('人口流动 （单位：万人）', [list(z) for z in zip(df['city'], df['value'])], '河南')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='河南省各市人口流入流出情况'),
        visualmap_opts=opts.VisualMapOpts(min_=-300, max_=300, range_text=['流入', '流出'], pos_left="8%"),
        tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"),  # 配置提示框，显示在数据项上
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"dataView": {"readOnly": False}}),  # 配置工具箱，显示并可编辑数据
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)

# 显示图表
map_chart.render("henanMap.html")
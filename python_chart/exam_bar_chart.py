# 部分省市高考人数与本科上线率对比图
from pyecharts.charts import Bar, Line
from pyecharts import options as opts

# 定义数据
data = [
    {"地区": "河南", "高考人数": 125, "本科录取率": 37.0},
    {"地区": "山东", "高考人数": 80, "本科录取率": 43.10},
    {"地区": "广东", "高考人数": 78, "本科录取率": 39.90},
    {"地区": "四川", "高考人数": 70, "本科录取率": 35.0},
    {"地区": "河北", "高考人数": 65, "本科录取率": 41.0},
    {"地区": "湖南", "高考人数": 58, "本科录取率": 32.05},
    {"地区": "广西", "高考人数": 55, "本科录取率": 32.34},
    {"地区": "安徽", "高考人数": 53, "本科录取率": 41.90},
    {"地区": "江苏", "高考人数": 36, "本科录取率": 59.20},
    {"地区": "浙江", "高考人数": 32, "本科录取率": 50.0},
    {"地区": "山西", "高考人数": 32, "本科录取率": 44.70},
    {"地区": "上海", "高考人数": 7, "本科录取率": 70.0},
    {"地区": "天津", "高考人数": 6, "本科录取率": 81.60},
    {"地区": "北京", "高考人数": 5, "本科录取率": 83.80}
]

# 转换数据格式
x_data = [item["地区"] for item in data]
y1_data = [item["高考人数"] for item in data]  # 高考人数转为万人单位
y2_data = [item["本科录取率"] for item in data]

# 创建 Bar 实例
bar = (
    Bar()
    # 添加 x 轴数据和 y 轴数据
    .add_xaxis(x_data)
    .add_yaxis(
        "高考人数（万人）",
        y1_data,
        yaxis_index=0,
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="本科录取率（%）",
            type_="value",
            position="right",
            axislabel_opts=opts.LabelOpts(formatter="{value}%"),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各地区高考人数与本科录取率对比图", subtitle="数据来源：教育部"),
        legend_opts=opts.LegendOpts(pos_left="40%"),
        xaxis_opts=opts.AxisOpts(splitline_opts=None),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={
            "dataZoom": {"yAxisIndex": "none"},
            "restore": {},
            "saveAsImage": {}
        })
    )
)

# 创建 Line 实例
line = (
    Line()
    # 添加 x 轴数据和 y 轴数据
    .add_xaxis(x_data)
    .add_yaxis(
        "本科录取率（%）",
        y2_data,
        yaxis_index=1,
        label_opts=opts.LabelOpts(position="left"),
        z=2
    )
)

# 将 Bar 和 Line 图表组合在一起
chart = bar.overlap(line)

# 渲染图像并保存到文件
chart.render("exam_bar_line_chart.html")



# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# # 数据
# data = [("河南", 125, 37),
#         ("山东", 80, 43.1),
#         ("广东", 78, 39.9),
#         ("四川", 70, 35),
#         ("河北", 65, 41),
#         ("湖南", 58, 32.05),
#         ("广西", 55, 32.34),
#         ("安徽", 53, 41.9),
#         ("江苏", 36, 59.2),
#         ("浙江", 32, 50),
#         ("山西", 32, 44.7),
#         ("上海", 7, 70),
#         ("天津", 6, 81.6),
#         ("北京", 5, 83.8)]
#
# # 创建柱状图
# bar = Bar()
#
# # 添加数据
# bar.add_xaxis([item[0] for item in data])
# bar.add_yaxis("高考人数", [item[1] for item in data], category_gap=2)
# bar.add_yaxis("本科录取率", [item[2] for item in data], category_gap=2)
#
# # 设置全局配置项
# bar.set_global_opts(title_opts=opts.TitleOpts(title="双向柱状图"))
#
# # 渲染图表
# bar.render("double_bar_chart.html")

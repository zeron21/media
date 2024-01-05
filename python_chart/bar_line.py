#全国流动人口统计柱状折线图
from pyecharts.charts import Bar, Line
from pyecharts import options as opts

# 定义地区列表和对应的指标数据
regions = ['上海', '北京', '天津', '浙江', '广东', '新疆', '江苏', '福建', '西藏', '海南',
           '宁夏', '内蒙古', '青海', '重庆', '辽宁', '陕西', '云南', '山西', '河北', '吉林',
           '山东', '湖北', '四川', '甘肃', '贵州', '江西', '广西', '黑龙江', '安徽', '湖南', '河南']
population = [2487.09, 2189.31, 1386.6, 6456.76, 12601.25, 2585.23, 8474.8, 4154.01, 364.81, 1008.12,
              720.27, 2404.92, 592.4, 3205.42, 4259.14, 3952.9, 4720.93, 3491.56, 7461.02, 2407.35,
              10152.75, 5775.26, 8367.49, 2501.98, 3856.21, 4518.86, 5012.68, 3785.01, 6102.72, 6644.49, 9936.55]
internal = [0, 0, 0, 937.1, 2244.4, 466.07, 1335.51, 877.14, 48.51, 157.41,
            183.19, 738.2, 118.87, 261.78, 714.59, 734.02, 836.87, 805.33, 1217.77, 694.99,
            1661.43, 1051.46, 1809.85, 457.59, 844.35, 835.5, 816.31, 765.27, 1232.18, 1259.45, 1992.81]
external = [1047.97, 841.84, 353.48, 1618.65, 2962.21, 339.07, 10030.86, 488.99, 40.71, 108.81,
            67.51, 168.64, 41.73, 219.36, 284.73, 193.37, 223.04, 162.05, 315.53, 100.15,
            412.9, 244.96, 259, 76.56, 114.65, 127.9, 135.94, 82.92, 155.05, 157.76, 127.36]
percentage = [42.10, 38.50, 25.50, 25.10, 23.50, 13.10, 12.20, 11.80, 11.20, 10.80,
              9.40, 7.00, 7.00, 6.80, 6.70, 4.90, 4.70, 4.60, 4.20, 4.20,
              4.10, 3.90, 3.10, 3.10, 3.00, 2.80, 2.70, 2.60, 2.50, 2.40, 1.30]

# # 按照省外流动人口降序排列
# data = sorted(zip(regions, population, internal, external, percentage), key=lambda x: x[3], reverse=True)
# regions, population, internal, external, percentage = zip(*data)

# 创建柱状图实例
bar = (
    Bar()
    .add_xaxis(regions)
    .add_yaxis("常住人口", population)
    .add_yaxis("省内流动人口", internal)
    .add_yaxis("省外流动人口", external)
    .extend_axis(yaxis=opts.AxisOpts(name="省外流动人口占比", position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国流动人口统计"),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45},splitline_opts=None),
        yaxis_opts=opts.AxisOpts(name="人口（单位：万人）"),  # 修改纵坐标标签
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {}
                })
    )
)

# 创建折线图实例
line = (
    Line()
    .add_xaxis(regions)
    .add_yaxis("省外流动人口占比", percentage, yaxis_index=1,z=2)
)

# 合并柱状图和折线图
bar.overlap(line)

# 生成HTML文件
bar.render("bar_line_chart.html")

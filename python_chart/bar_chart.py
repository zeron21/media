# 第七次人口普查各省流出人口统计图
from pyecharts.charts import Bar
from pyecharts import options as opts

# 定义数据
provinces = ["河南", "安徽", "四川", "贵州", "广西", "湖南", "江西", "湖北", "河北", "江苏",
             "山东", "重庆", "黑龙江", "甘肃", "陕西", "云南", "福建", "吉林", "浙江", "陕西",
             "辽宁", "内蒙古", "广东", "天津", "新疆", "北京", "青海", "海南", "上海", "宁夏", "西藏"]
data = [1610.1, 1152.1, 1035.8, 845.5, 810.9, 804.1, 634.0, 598.6, 548.0, 435.2,
        425.9, 417.6, 393.2, 344.8, 298.8, 296.2, 261.4, 241.4, 236.2, 198.5,
        187.4, 177.8, 168.7, 79.9, 60.3, 47.0, 43.1, 42.3, 38.4, 36.6, 13.8]

# 创建柱状图实例
bar = (
    Bar()
    .add_xaxis(provinces)
    .add_yaxis("流出人口", data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各省流出人口"),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45},splitline_opts=None),
        yaxis_opts=opts.AxisOpts(name="流出人口（单位：万人）"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={
            "dataZoom": {"yAxisIndex": "none"},
            "restore": {},
            "saveAsImage": {}
        })
    )
)

# 生成HTML文件
bar.render("outflow_bar_chart.html")

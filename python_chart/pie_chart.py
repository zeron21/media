from pyecharts.charts import Pie
from pyecharts import options as opts

# 定义数据
provinces = ["安徽", "山东", "河北", "湖北", "四川", "陕西", "江苏", "山西", "浙江", "福建"]
data = [14.2, 12.4, 10.6, 9.5, 7.1, 7.0, 6.7, 5.7, 4.9, 4.3]

# 创建饼状图实例
pie = (
    Pie()
    .add("", [list(z) for z in zip(provinces, data)])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="河南省流入人口来源地"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="43%", pos_left="8%")

    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}万人"))
)

# 生成HTML文件
pie.render("inflow_pie_chart.html")

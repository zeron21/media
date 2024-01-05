# 河南人口流出到各省桑基图
from pyecharts.charts import Sankey
from pyecharts import options as opts

# 定义数据
source = ["河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南",
          "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南",
          "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南"]
target = ["广东", "浙江", "江苏", "上海", "北京", "新疆", "山东", "天津", "福建", "河北",
          "湖北", "陕西", "山西", "安徽", "辽宁", "四川", "湖南", "甘肃", "云南", "内蒙古",
          "江西", "海南", "重庆", "广西", "宁夏", "吉林", "贵州", "黑龙江", "西藏"]
value = [277.36, 246.59, 219.72, 134.30, 127.19, 73.89, 62.93, 55.32, 50.61, 50.48,
         47.81, 36.96, 36.49, 30.37, 20.71, 19.18, 13.37, 12.24, 11.85, 11.70,
         11.58, 8.56, 8.38, 7.62, 6.71, 6.53, 5.55, 5.48, 3.12]


# 创建桑基图实例
sankey = (
    Sankey()
    .add("",
         nodes=[{"name": "河南"}, {"name": "广东"}, {"name": "浙江"}, {"name": "江苏"}, {"name": "上海"},
                {"name": "北京"}, {"name": "新疆"}, {"name": "山东"}, {"name": "天津"}, {"name": "福建"},
                {"name": "河北"}, {"name": "湖北"}, {"name": "陕西"}, {"name": "山西"}, {"name": "安徽"},
                {"name": "辽宁"}, {"name": "四川"}, {"name": "湖南"}, {"name": "甘肃"}, {"name": "云南"},
                {"name": "内蒙古"}, {"name": "江西"}, {"name": "海南"}, {"name": "重庆"}, {"name": "广西"},
                {"name": "宁夏"}, {"name": "吉林"}, {"name": "贵州"}, {"name": "黑龙江"}, {"name": "西藏"}],
         links=[{"source": "河南", "target": "广东", "value": 277.36},
                {"source": "河南", "target": "浙江", "value": 246.59},
                {"source": "河南", "target": "江苏", "value": 219.72},
                {"source": "河南", "target": "上海", "value": 134.30},
                {"source": "河南", "target": "北京", "value": 127.19},
                {"source": "河南", "target": "新疆", "value": 73.89},
                {"source": "河南", "target": "山东", "value": 62.93},
                {"source": "河南", "target": "天津", "value": 55.32},
                {"source": "河南", "target": "福建", "value": 50.61},
                {"source": "河南", "target": "河北", "value": 50.48},
                {"source": "河南", "target": "湖北", "value": 47.81},
                {"source": "河南", "target": "陕西", "value": 36.96},
                {"source": "河南", "target": "山西", "value": 36.49},
                {"source": "河南", "target": "安徽", "value": 30.37},
                {"source": "河南", "target": "辽宁", "value": 20.71},
                {"source": "河南", "target": "四川", "value": 19.18},
                {"source": "河南", "target": "湖南", "value": 13.37},
                {"source": "河南", "target": "甘肃", "value": 12.24},
                {"source": "河南", "target": "云南", "value": 11.85},
                {"source": "河南", "target": "内蒙古", "value": 11.70},
                {"source": "河南", "target": "江西", "value": 11.58},
                {"source": "河南", "target": "海南", "value": 8.56},
                {"source": "河南", "target": "重庆", "value": 8.38},
                {"source": "河南", "target": "广西", "value": 7.62},
                {"source": "河南", "target": "宁夏", "value": 6.71},
                {"source": "河南", "target": "吉林", "value": 6.53},
                {"source": "河南", "target": "贵州", "value": 5.55},
                {"source": "河南", "target": "黑龙江", "value": 5.48},
                {"source": "河南", "target": "西藏", "value": 3.12}],

         linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
         label_opts=opts.LabelOpts(position="right"))

    .set_global_opts(
        title_opts=opts.TitleOpts(title="河南人口流出到各省的桑基图"),
        tooltip_opts=opts.TooltipOpts(trigger_on="mousemove|click", axis_pointer_type="cross")
    )
)

# 生成HTML文件
sankey.render("henan_sankey_chart.html")

# from pyecharts.charts import Sankey
# from pyecharts import options as opts
#
# # 定义数据
# source = ["河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南",
#           "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南",
#           "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南", "河南"]
# target = ["广东", "浙江", "江苏", "上海", "北京", "新疆", "山东", "天津", "福建", "河北",
#           "湖北", "陕西", "山西", "安徽", "辽宁", "四川", "湖南", "甘肃", "云南", "内蒙古",
#           "江西", "海南", "重庆", "广西", "宁夏", "吉林", "贵州", "黑龙江", "西藏"]
# value = [277.36, 246.59, 219.72, 134.30, 127.19, 73.89, 62.93, 55.32, 50.61, 50.48,
#          47.81, 36.96, 36.49, 30.37, 20.71, 19.18, 13.37, 12.24, 11.85, 11.70,
#          11.58, 8.56, 8.38, 7.62, 6.71, 6.53, 5.55, 5.48, 3.12]
#
# # 将河南的流出量减半，添加一个与河南流出量相等的值作为河南流入其他省份的量
# source_value = [i / 2 for i in value]
# target_value = [i / 2 for i in value]
# target_value.append(sum(value) / 2)
#
# # 创建桑基图实例
# sankey = (
#     Sankey()
#     .add("",
#          nodes=[{"name": "河南"}, {"name": "广东"}, {"name": "浙江"}, {"name": "江苏"}, {"name": "上海"},
#                 {"name": "北京"}, {"name": "新疆"}, {"name": "山东"}, {"name": "天津"}, {"name": "福建"},
#                 {"name": "河北"}, {"name": "湖北"}, {"name": "陕西"}, {"name": "山西"}, {"name": "安徽"},
#                 {"name": "辽宁"}, {"name": "四川"}, {"name": "湖南"}, {"name": "甘肃"}, {"name": "云南"},
#                 {"name": "内蒙古"}, {"name": "江西"}, {"name": "海南"}, {"name": "重庆"}, {"name": "广西"},
#                 {"name": "宁夏"}, {"name": "吉林"}, {"name": "贵州"}, {"name": "黑龙江"}, {"name": "西藏"}],
#          links=[{"source": "河南", "target": "广东", "value": value[0]},
#                 {"source": "河南", "target": "浙江", "value": value[1]},
#                 {"source": "河南", "target": "江苏", "value": value[2]},
#                 {"source": "河南", "target": "上海", "value": value[3]},
#                 {"source": "河南", "target": "北京", "value": value[4]},
#                 {"source": "河南", "target": "新疆", "value": value[5]},
#                 {"source": "河南", "target": "山东", "value": value[6]},
#                 {"source": "河南", "target": "天津", "value": value[7]},
#                 {"source": "河南", "target": "福建", "value": value[8]},
#                 {"source": "河南", "target": "河北", "value": value[9]},
#                 {"source": "河南", "target": "湖北", "value": value[10]},
#                 {"source": "河南", "target": "陕西", "value": value[11]},
#                 {"source": "河南", "target": "山西", "value": value[12]},
#                 {"source": "河南", "target": "安徽", "value": value[13]},
#                 {"source": "河南", "target": "辽宁", "value": value[14]},
#                 {"source": "河南", "target": "四川", "value": value[15]},
#                 {"source": "河南", "target": "湖南", "value": value[16]},
#                 {"source": "河南", "target": "甘肃", "value": value[17]},
#                 {"source": "河南", "target": "云南", "value": value[18]},
#                 {"source": "河南", "target": "内蒙古", "value": value[19]},
#                 {"source": "河南", "target": "江西", "value": value[20]},
#                 {"source": "河南", "target": "海南", "value": value[21]},
#                 {"source": "河南", "target": "重庆", "value": value[22]},
#                 {"source": "河南", "target": "广西", "value": value[23]},
#                 {"source": "河南", "target": "宁夏", "value": value[24]},
#                 {"source": "河南", "target": "吉林", "value": value[25]},
#                 {"source": "河南", "target": "贵州", "value": value[26]},
#                 {"source": "河南", "target": "黑龙江", "value": value[27]},
#                 {"source": "河南", "target": "西藏", "value": value[28]},
#                 {"source": "河南", "target": "河南", "value": sum(value) / 2}],  # 河南流入自身的量
#          linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
#          label_opts=opts.LabelOpts(position="right"))
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="河南人口流出到各省的桑基图"),
#         tooltip_opts=opts.TooltipOpts(trigger_on="mousemove|click", axis_pointer_type="cross",
#                                       formatter="{b}: 1610")  # 修改tooltip显示内容
#     )
# )
#
# # 生成HTML文件
# sankey.render("henan_sankey_chart2.html")


<template>
  <div class="app-container">
    <div class="filter-container">

      <div id="chartPie" class="pie-wrap"></div>
      <Kanban :key="1" :list="list1" :group="group" class="kanban todo" />
      <Kanban :key="2" :list="list2" :group="group" class="kanban todo" />
      <div class="result">
        <img
          v-if="status === true"
          src='@/assets/success.svg'
          class="result images"
        />
        <img v-else src='@/assets/fail.svg' class="images"/>
        <h1 v-if="status === true" class="result text">vulnerable</h1>
        <h1 v-else class="result text">invulnerable</h1>
      </div>
      <div class="scan-details">
        <el-table
          :data="urlList"
          style="width: 100%;margin-top:10px"
          :row-key="getRowKeys"
          :expand-row-keys="expands"
          @current-change="toggleRowExpansion">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-row :gutter="16">
                  <el-col :xs="{span: 24}" :sm="{span: 8}" :md="{span: 8}" :lg="{span: 8}" :xl="{span: 8}">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px">目标网址</el-tag>
                      <span>{{ props.row.url }}</span>
                    </el-form-item>
                  </el-col>
                  <el-col :xs="{span: 24}" :sm="{span: 16}" :md="{span: 16}" :lg="{span: 16}" :xl="{span: 16}">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px">Payload Demo</el-tag>
                      <span>{{ props.row.payload }}</span>
                    </el-form-item>
                  </el-col>
                </el-row>
                <el-row :gutter="16">
                  <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 8}" :xl="{span: 8}">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px">GET参数</el-tag>
                      <span v-if="props.row.vulnArgs.length > 0">{{ props.row.vulnArgs }}</span>
                      <span v-else>无</span>
                    </el-form-item>
                  </el-col>
                  <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 8}" :xl="{span: 8}">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px" >POST参数</el-tag>
                      <span v-if="props.row.param.length > 0">{{ props.row.param }}</span>
                      <span v-else>无</span>
                    </el-form-item>
                  </el-col>
                  <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 8}" :xl="{span: 8}">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px">Headers</el-tag>
                      <span v-if="props.row.vulnHeader.length > 0">{{ props.row.vulnHeader }}</span>
                      <span v-else>无</span>
                    </el-form-item>
                  </el-col>
                </el-row>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column
            label="Vulnerable URL"
            style="width: 80%"
            prop="url">
          </el-table-column>
        </el-table>
      </div>

    </div>
  </div>
</template>

<script>
import echarts from 'echarts'
import Kanban from '@/components/Kanban'

require('echarts/theme/macarons')
export default {
  components: {
    Kanban
  },
  created() {
    const response = this.$route.params.response
    this.urlList = response.data.vuln
    this.list2[0].end = response.data.payloads
    this.list1[0].end = response.data.time
    this.list1[1].end = response.data.total
    this.list2[1].end = response.data.vuln.length
    this.vulnNum = response.data.vuln.length
    this.unvulnNum = response.data.unvuln.length
    this.status = response.data.status
    console.log(response)
  },
  data() {
    return {
      status: false,
      payload: 0,
      lineChartData: [],
      urlList: [],
      vulnNum: 0,
      unvulnNum: 0,
      getRowKeys(row) {
        return row.id
      },
      form: {},
      // 要展开的行，数值的元素是row的key值
      expands: [],

      group: 'mission',
      list1: [
        { name: 'Time', id: 1, start: 0, end: 0, icons: 'time' },
        { name: 'Total', id: 2, start: 0, end: 0, icons: 'total' }
      ],
      list2: [
        { name: 'Payloads  ', id: 1, start: 0, end: 0, icons: 'payload' },
        { name: 'Vulnerable', id: 2, start: 0, end: 0, icons: 'vulnerable' }
      ]
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.drawPieChart()
    })
  },
  methods: {
    drawPieChart() {
      this.chartPie = echarts.init(
        document.getElementById('chartPie'),
        'macarons'
      )
      this.chartPie.setOption({
        title: {
          text: '漏洞网址分布图',
          subtext: '百分比图',
          x: 'center',
          y: 'top'
        },
        // 显示在上面的文字
        tooltip: {
          trigger: 'item',
          formatter: '{b}: <br/>{c}({d}%)'
        },
        legend: {
          data: ['vulnerable', 'invulnerable'],
          right: 500,
          orient: 'horizontal',
          x: 'center',
          y: 'bottom'
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            // 圆圈的粗细
            radius: ['35%', '60%'],
            // 圆圈的位置
            center: ['50%', '55%'],
            data: [
              {
                value: this.vulnNum,
                name: 'vulnerable'
              },
              {
                value: this.unvulnNum,
                name: 'invulnerable'
              }
            ],
            // 动画持续时间：2秒
            animationDuration: 2000,
            // 控制是否显示指向文字的,默认为true
            label: {
              position: 'left',
              show: false,
              formatter: '{b} : {c} ({d}%)',
              textStyle: {
                color: '#333',
                fontSize: 14
              }
            }
          }
        ]
      })
    },
    handleClick(tab) {
      // console.log(tab)
    },
    toggleRowExpansion(row) {
      this.expands = []
      this.expands.push(row.id)
    }
  }
}
</script>

<style lang="scss" scoped>
.pie-wrap {
  width: 30%;
  margin-right: -3%;
  margin-left: -3%;
  height: 300px;
  display: inline-block;
}

.scan-details{
  margin-top: 30px;
  width: 100%
}

.kanban {
  width: 20%;
  height: 300px;
  display: inline-block;
  &.todo {
    .board-column-header {
      background: #4A9FF9;
    }
  }
}

.result {
  width: 30%;
  height: 300px;
  margin-left: -5%;
  display: inline-block;

  .images{
    width: 65%;
    height: 65%;
    margin-top: 0px;
    margin-left: 30%;
    margin-bottom: 15%;
  }
  .text{
    margin-top: -45%;
    margin-left: 41%;
    margin-bottom: 45%;
  }
}
</style>

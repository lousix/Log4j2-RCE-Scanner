<template>
  <div class="app-container">
    <div class="filter-container">
      <el-tabs v-model="usable" :tab-position="tabPosition" @tab-click="handleClick">
        <el-tab-pane v-for="(tab,index) in tabs" :key="index" :name="tab.name" :label="tab.label">
          <div v-show="usable==='1'">
            <el-table
              :data="urlList"
              style="width: 100%;margin-top:10px"
              :row-key="getRowKeys"
              :expand-row-keys="expands"
              @current-change="toggleRowExpansion"
            >
              <el-table-column type="expand">
                <template slot-scope="props">
                  <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="">
                      <el-tag style="margin-right: 10px">目标网址</el-tag>
                      <span>{{ props.row.url }}</span>
                    </el-form-item>
                    <p>
                      <el-form-item label="">
                        <el-tag style="margin-right: 10px">GET参数</el-tag>
                        <span v-if="props.row.args.length > 0">{{ props.row.args }}</span>
                        <span v-else>无</span>
                      </el-form-item>
                      <el-form-item style="margin-left: 30%" label="">
                        <el-tag style="margin-right: 10px">POST参数</el-tag>
                        <span v-if="props.row.param.length > 0">{{ props.row.param }}</span>
                        <span v-else>无</span>
                      </el-form-item>
                    </p>
                    <p />
                  </el-form>
                </template>
              </el-table-column>
              <el-table-column
                label="需要扫描的网址"
                style="width: 80%"
                prop="url"
              />
            </el-table>
          </div>
          <div v-show="usable==='2'">
            <el-col>
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>Headers</span>
                </div>
                <div class="component-item">
                  <p v-for="item in headerList">
                    <el-tag>{{ item.header }}</el-tag>
                    <span>{{ item.value }}</span>
                  </p>
                </div>
              </el-card>
            </el-col>
            <el-col>
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>CheckHeaders</span>
                </div>
                <div class="component-item">
                  <p v-for="item in checkHeader">
                    <span>{{ item }}</span>
                  </p>
                </div>
              </el-card>
            </el-col>
            <el-col>
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span>Payloads</span>
                </div>
                <div class="component-item">
                  <p v-for="item in payloadList">
                    {{ item }}
                  </p>
                </div>
              </el-card>
            </el-col>
          </div>
        </el-tab-pane>
      </el-tabs>
      <el-button class="attack_btn" @click="attack">attack</el-button>
    </div>
  </div>
</template>

<script>
import { attack } from '@/api/config'

export default {
  data() {
    return {
      tabPosition: 'top',
      usable: '1',
      tabs: [
        { name: '1', label: '扫描网址' },
        { name: '2', label: '扫描配置' },
        { name: '3', label: '扫描确认' }
      ],
      urlList: [],
      payloadList: [],
      headerList: [],
      checkHeader: [],
      getRowKeys(row) {
        return row.id
      },
      form: {},
      // 要展开的行，数值的元素是row的key值
      expands: []
    }
  },
  created() {
    const url = JSON.parse(sessionStorage.getItem('urlScan_data'))
    for (let i = 0; i < url.list.length; i++) {
      const item = url.list[i]
      if (item.status === 'check') {
        this.urlList.push(item)
      }
    }
    this.headerList = (JSON.parse(sessionStorage.getItem('headers_data'))).formData.domains

    const payloadList = JSON.parse(sessionStorage.getItem('payloads_data'))
    if (payloadList !== null) {
      for (let i = 0; i < payloadList.value.length; i++) {
        this.payloadList.push(payloadList.data[i].label)
      }
    }

    const checkHeader = JSON.parse(sessionStorage.getItem('checkHeaders_data'))
    if (checkHeader !== null) {
      for (let i = 0; i < checkHeader.value.length; i++) {
        this.checkHeader.push(checkHeader.data[i].label)
      }
    }
  },
  methods: {
    handleClick(tab) {
      // console.log(tab)
    },
    toggleRowExpansion(row) {
      this.expands = []
      this.expands.push(row.id)
    },
    attack() {
      attack({ 'urlList': this.urlList }).then(response => {
        this.$router.push({
          path: '/result',
          name: 'Result',
          params: {
            response: response
          }
        })
      })
    }
  }
}
</script>

<style scoped>
.box-card {
  width: 100%;
  max-width: 100%;
  margin: 20px auto;
}

.attack_btn{
  margin-top: 20px;
  margin-left: 45%;
  width: 200px;
}
</style>

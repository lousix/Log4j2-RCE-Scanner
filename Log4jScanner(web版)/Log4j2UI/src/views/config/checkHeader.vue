<template>
  <div class="createPost-container" style="text-align: center">
    <div class="createPost-main-container">
      <h2 style="text-align: center;">HTTP Headers 选定</h2>
      <el-transfer
        v-model="value"
        style="text-align: left; display: inline-block"
        filterable
        :left-default-checked="[]"
        :right-default-checked="[]"
        :render-content="renderFunc"
        :titles="['Payloads List', 'Payloads upload List']"
        :format="{
          noChecked: '0/${total}',
          hasChecked: '${checked}/${total}'
        }"
        :data="data"
        @change="handleChange">
        <div slot="left-footer" class="transfer-footer" align="center">
          <el-input v-model="payload" style="width: 350px; margin-right: 10px" placeholder="Headers to add" />
          <el-button class="filter-item" @click="addPayloads()">ADD</el-button>
        </div>
        <div slot="right-footer" class="transfer-footer" align="center">
          <el-button class="filter-item" type="primary" style="width: 250px" @click="upload()">upload</el-button>
        </div>
      </el-transfer>
    </div>
  </div>
</template>

<style>
.transfer-footer {
  margin-left: 20px;
  padding: 6px 5px;
}
</style>

<script>
import { uploadHeaders, headers } from '@/api/config'

export default {
  data() {
    const generateData = _ => {
      const data = []
      for (let i = 0; i < headers.length; i++) {
        data.push({
          key: i + 1,
          label: headers[i],
          disabled: false
        })
      }
      return data
    }
    return {
      data: generateData(),
      value: [],
      renderFunc(h, option) {
        return <span>{ option.label }</span>
      },
      payload: ''
    }
  },
  beforeDestroy() {
    sessionStorage.setItem('checkHeaders_data', JSON.stringify(this.$data))
  },
  created() {
    const data = JSON.parse(sessionStorage.getItem('checkHeaders_data'))
    if (data !== null) {
      Object.assign(this, data)
    }
  },

  methods: {
    handleChange(value, direction, movedKeys) {
      console.log(value, direction, movedKeys)
    },
    upload() {
      const list = []
      for (let i = 0; i < this.value.length; i++) {
        list.push(this.data[this.value[i] - 1].label)
      }
      // console.log(list)
      uploadHeaders({ 'headers': list }).then(response => {
        if (response.code === 20000) {
          this.$notify({
            title: 'Success',
            message: 'Upload Successfully',
            type: 'success',
            duration: 2000
          })
        } else {
          this.$notify({
            title: 'Fail',
            message: 'Upload Fail',
            type: 'fail',
            duration: 2000
          })
        }
      })
    },
    addPayloads() {
      this.data.push({
        key: this.data.length + 1,
        label: this.payload,
        disabled: false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/styles/mixin.scss";

.createPost-container {
  position: relative;

  .createPost-main-container {
    padding: 10px 45px 20px 50px;

    .postInfo-container {
      position: relative;
      @include clearfix;
      margin-bottom: 10px;

      .postInfo-container-item {
        float: left;
      }
    }
  }

  .word-counter {
    width: 40px;
    position: absolute;
    right: 10px;
    top: 0px;
  }
}

::v-deep .el-transfer-panel{
  width: 500px;
  height: 650px;
}
::v-deep .el-transfer-panel__list.is-filterable{
  height: 500px;
}
::v-deep .el-transfer__buttons{
  display: flow;
  align-items: center;
  justify-content: center;
  .el-button.el-button--primary{
    margin-left: 5px;
  }
}

::v-deep .el-transfer-panel__footer{
  height: 50px;
}
</style>

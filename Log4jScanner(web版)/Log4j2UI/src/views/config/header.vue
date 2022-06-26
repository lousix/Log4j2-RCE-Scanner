<template>
  <div class="app-container">
    <div class="filter-container">
      <el-form ref="formData" :model="formData" label-width="150px" class="form-dynamic">
        <el-form-item
          v-for="(domain, index) in formData.domains"
          :key="domain.key"
          :label="'Header No.' + (index+1)"
          :prop="'domains.' + index + '.value'"
        >
          <el-input v-model="domain.header" placeholder="KEY" style="width: 25%;margin-right: 5%" :rules="{required: true, message: '内容不能为空', trigger: 'blur'}"/>
          <el-input v-model="domain.value" placeholder="Value" style="width: 60%" :rules="{required: true, message: '内容不能为空', trigger: 'blur'}"/>
          <a v-show="formData.domains.length>1" style="margin-left: 10px;" class="remove-item" @click.prevent="removeDomain(domain)"><i  class="el-icon-delete" /></a>
        </el-form-item>
        <el-form-item class="submit-btn">
          <el-button type="primary" @click="submitForm('formData')">提交</el-button>
          <el-button @click="addDomain">新增一项</el-button>
          <el-button @click="resetForm('formData')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { header } from '@/api/config'

export default {
  name: 'Form',
  data() {
    return {
      formData: {
        domains: [{
          header: '',
          value: ''
        }]
      }
    }
  },
  methods: {
    /* 增加表单项*/
    addDomain() {
      this.formData.domains.push({
        header: '',
        value: ''
      })
    },
    /* 删除表单项*/
    removeDomain(item) {
      var index = this.formData.domains.indexOf(item)
      if (index !== -1) {
        this.formData.domains.splice(index, 1)
      }
    },
    /* 格式化表单数据*/
    formatData(data) { // 动态表单生成的是一个对象数组，需要把对象数组转成一个对象
      const obj = {}
      data.forEach((item) => {
        obj[item.header] = item.value
      })
      return obj
    },
    /* 提交表单*/
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const headerData = this.formatData(this.formData.domains)
          header({ 'headers': headerData }).then(response => {
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
        } else {
          this.$alert('表单项不能为空', { dangerouslyUseHTMLString: true })
          return false
        }
      })
    },
    /* 重置表单*/
    resetForm(formName) {
      this.$refs[formName].resetFields()
    }
  },
  beforeDestroy() {
    sessionStorage.setItem('headers_data', JSON.stringify(this.$data))
  },
  created() {
    const data = JSON.parse(sessionStorage.getItem('headers_data'))
    if (data !== null) {
      Object.assign(this, data)
    }
  }
}
</script>

<style scoped>
.form-dynamic{
  width: 100%;
  background: #fff;
  padding: 20px;
  padding-top: 40px;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  text-align: center;
}
.el-input{
  width: 95%;
}
.remove-item{
  color: red;
}
.submit-btn{
  text-align: center;
  margin-left: -10%;
}
</style>

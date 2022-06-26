<template>
  <div class="app-container">
    <div class="filter-container">
      Target Website : <el-input v-model="listQuery.url" placeholder="TARGET WEBSITE" style="width: 300px;margin-right: 20px" class="filter-item" @keyup.enter.native="handleFilter" />
      Thread Number : <el-input v-model="listQuery.threadNum" placeholder="Thread Num" style="width: 100px;margin-right: 30px" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Scan
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list.slice((tableConfig.page-1)*tableConfig.size,tableConfig.page*tableConfig.size)"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="URL" min-width="150px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.url }}</span>
        </template>
      </el-table-column>
      <el-table-column label="POST_Params" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.param }}</span>
        </template>
      </el-table-column>
      <el-table-column label="GET_Params" width="110px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.args }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Status" class-name="status-col" width="100">
        <template slot-scope="{row}">
          <el-tag :type="row.status | statusFilter">
            {{ row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Actions" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
          <el-button v-if="row.status!=='check'" size="mini" type="success" @click="handleModifyStatus(row,'check')">
            Check
          </el-button>
          <el-button v-if="row.status!=='drop'" size="mini" @click="handleModifyStatus(row,'drop')">
            Drop
          </el-button>
          <el-button v-if="row.status!=='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-pagination
      v-show="total>0"
      :total="total"
      :current-page="tableConfig.page"
      :page-sizes="tableConfig.sizes"
      :page-size="tableConfig.size"
      layout="total, sizes, prev, pager, next, jumper"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="URL" prop="URL">
          <el-input v-model="temp.url" placeholder="TARGET URL" />
        </el-form-item>
        <el-form-item label="GET" prop="GET">
          <el-input v-model="temp.args" placeholder="Please pick a date" />
        </el-form-item>
        <el-form-item label="POST" prop="POST">
          <el-input v-model="temp.param" />
        </el-form-item>
        <el-form-item label="Status">
          <el-select v-model="temp.status" class="filter-item" placeholder="Please select">
            <el-option v-for="item in statusOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { fetchList, fetchPv } from '@/api/article'
import waves from '@/directive/waves' // waves directive
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

const calendarTypeOptions = [
  { key: 'CN', display_name: 'China' },
  { key: 'US', display_name: 'USA' },
  { key: 'JP', display_name: 'Japan' },
  { key: 'EU', display_name: 'Eurozone' }
]

// arr to obj, such as { CN : "China", US : "USA" }
const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name
  return acc
}, {})

export default {
  name: 'ComplexTable',
  // eslint-disable-next-line vue/no-unused-components
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        check: 'success',
        drop: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type]
    }
  },
  data() {
    return {
      // tableData:[],
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      tableConfig: {
        page: 1,
        size: 20,
        sizes: [10, 20, 30, 50]
      },
      listQuery: {
        url: '',
        threadNum: '5'
      },
      importanceOptions: [1, 2, 3],
      calendarTypeOptions,
      // sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['check', 'drop'],
      showReviewer: false,
      temp: {
        id: undefined,
        url: '',
        param: '',
        origin: '',
        args: '',
        status: 'check'
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        URL: [{ message: 'url is required', trigger: 'blur' }],
        GET: [{ message: 'timestamp is required' }],
        POST: [{ message: 'title is required' }]
      },
      downloadLoading: false
    }
  },
  beforeDestroy() {
    sessionStorage.setItem('urlScan_data', JSON.stringify(this.$data))
  },
  created() {
    const data = JSON.parse(sessionStorage.getItem('urlScan_data'))
    if (data !== null) {
      Object.assign(this, data)
    } else {
      this.getList()
    }
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total

        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      })
    },
    handleSizeChange(val) {
      // 改变每页显示的条数
      this.tableConfig.size = val
      // 注意：在改变每页显示的条数时，要将页码显示到第一页
      this.tableConfig.page = 1
    },
    // 显示第几页
    handleCurrentChange(val) {
      // 改变默认的页数
      this.tableConfig.page = val
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: '操作Success',
        type: 'success'
      })
      row.status = status
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        url: '',
        args: '',
        param: '',
        origin: '',
        status: 'check'
      }
    },
    handleCreate() {
      this.dialogStatus = 'create'
      this.resetTemp()
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(this.total + 1) // mock a id
          this.total = this.total + 1

          this.list.push(this.temp)
          this.dialogFormVisible = false
          this.$notify({
            title: 'Success',
            message: 'Created Successfully',
            type: 'success',
            duration: 2000
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          // const tempData = Object.assign({}, this.temp)
          const index = this.list.findIndex(v => v.id === this.temp.id)
          this.list.splice(index, 1, this.temp)
          this.dialogFormVisible = false
          this.$notify({
            title: 'Success',
            message: 'Update Successfully',
            type: 'success',
            duration: 2000
          })
        }
      })
    },
    handleDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    },
    handleFetchPv(pv) {
      fetchPv(pv).then(response => {
        this.pvData = response.data.pvData
        this.dialogPvVisible = true
      })
    },
    formatJson(filterVal) {
      return this.list.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    }
  }
}
</script>

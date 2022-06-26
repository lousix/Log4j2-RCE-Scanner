<template>
  <el-card class="box-card-component" style="margin-left:8px;">
    <div slot="header" class="box-card-header">
      <img src="@/assets/log4j2.jpeg">
    </div>
    <div style="position:relative;">
      <mallki class-name="mallki-text" text="Basics" />
      <div style="padding-top:35px;" >
        <h4>CVE编号: </h4>
        <span class="progress-item">CVE-2021-44228</span>
      </div>
      <div>
        <h4>风险等级: </h4>
        <el-rate style="margin-left: 5%" :disabled='true' :show-text="true" :texts="['低危','中低危','中危','中高危','高危']" :value=5>
        </el-rate>
      </div>
      <div>
        <h4>受影响版本: </h4>
        <span class="progress-item">Apache log4j2 >= 2.0, <= 2.14.1</span>
      </div>
      <div>
        <h4>安全版本: </h4>
        <span class="progress-item">Apache log4j2 2.16.0</span>
      </div>
    </div>
  </el-card>
</template>

<script>
import { mapGetters } from 'vuex'
import PanThumb from '@/components/PanThumb'
import Mallki from '@/components/TextHoverEffect/Mallki'

export default {
  components: { PanThumb, Mallki },

  filters: {
    statusFilter(status) {
      const statusMap = {
        success: 'success',
        pending: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      statisticsData: {
        article_count: 1024,
        pageviews_count: 1024
      }
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])
  }
}
</script>

<style lang="scss" >
.box-card-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style lang="scss" scoped>
.box-card-component {
  .box-card-header {
    position: relative;
    height: 110px;
    img {
      width: 100%;
      height: 100%;
      transition: all 0.2s linear;
      &:hover {
        transform: scale(1.1, 1.1);
        filter: contrast(130%);
      }
    }
  }
  .mallki-text {
    position: absolute;
    top: 0px;
    right: 0px;
    font-size: 25px;
    font-weight: bold;
  }
  .panThumb {
    z-index: 100;
    height: 70px!important;
    width: 70px!important;
    position: absolute!important;
    top: -45px;
    left: 0px;
    border: 5px solid #ffffff;
    background-color: #fff;
    margin: auto;
    box-shadow: none!important;
    ::v-deep .pan-info {
      box-shadow: none!important;
    }
  }
  .progress-item {
    margin-top: -20px;
    margin-left: 5%;
    margin-bottom: -10px;
    font-size: 14px;
    display: inline-block;
    font-family: "微软雅黑"
  }
  @media only screen and (max-width: 1510px){
    .mallki-text{
      display: none;
    }
  }
}
</style>

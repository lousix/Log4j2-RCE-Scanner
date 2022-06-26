<template>
  <el-card class="box-card2-component" style="margin-left:8px;">
    <div slot="header" class="box-card-header">
      <img src="@/assets/detail.jpeg">
    </div>
    <div style="position:relative;">
      <mallki class-name="mallki-text" text="Vulnerability Details" />
      <div style="padding-top:35px;" >
        <h4>漏洞详情: </h4>
        <span class="progress-item">&nbsp;&nbsp;Apache Log4j2 2.0-beta9 到 2.15.0（不包括安全版本 2.12.2、2.12.3 和 2.3.1）配置、日志消息和参数中使用的 JNDI 功能不能防止攻击者控制的 LDAP 和其他 JNDI 相关端点。当启用消息查找替换时，可以控制日志消息或日志消息参数的攻击者可以执行从 LDAP 服务器加载的任意代码。从 log4j 2.15.0 开始，默认情况下已禁用此行为。从版本 2.16.0（以及 2.12.2、2.12.3 和 2.3.1）开始，此功能已被完全删除。请注意，此漏洞特定于 log4j-core，不会影响 log4net、log4cxx 或其他 Apache Logging Services 项目。</span>
      </div>
      <div>
        <h4>受影响版本: </h4>
        <span class="progress-item">Apache Struts2, Apache Solr, Apache Druid, Apache Flink, Apache Flume, Apache Dubbo, Apache Kafka</span>
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
.box-card2-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style lang="scss" scoped>
.box-card2-component {
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
    line-height: 1.26em;
    margin-left: 5%;
    margin-top: -5px;
    margin-bottom: 5px;
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

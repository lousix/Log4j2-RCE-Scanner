<template>
  <el-card class="box-card2-component" style="margin-left:8px;">
    <div slot="header" class="box-card-header">
      <img src="@/assets/detail.jpeg">
    </div>
    <div style="position:relative;">
      <mallki class-name="mallki-text" text="Repair Recommendations" />
      <div style="padding-top:35px;" >
        <h4>修复建议: </h4>
        <span class="progress-item">
          （1）添加jvm启动参数-D log4j2.formatMsgNoLookups=true<br><br>
          （2）在应用classpath下添加log4j2.component.properties配置文件，文件内容为log4j2.formatMsgNoLookups=true<br><br>
          （3）JDK使用11.0.1、8u191、7u201、6u211及以上的高版本<br><br>
          （4）限制受影响应用对外访问互联网<br><br>
          （5）禁用JNDI，如在spring.properties里添加spring.jndi.ignore=true<br><br>
          （6）部署使用第三方防火墙产品进行安全防护，并更新WAF、RASP规则等，实时监测网络流量，匹配过滤恶意请求<br>
        </span>
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
    line-height: 1.3em;
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

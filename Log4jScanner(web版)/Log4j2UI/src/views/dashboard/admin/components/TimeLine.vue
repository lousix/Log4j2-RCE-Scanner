<template>
  <el-timeline>
    <el-timeline-item
      v-for="(activity, index) in activities"
      :key="index"
      :icon="activity.icon"
      :type="activity.type"
      :size="activity.size"
    >
      <div>
        <div class="el-row">
          <div class="fl"> <strong>{{activity.timestamp}}</strong></div><br>
          <a style="color: #909399;">{{activity.content}}</a>
        </div>

      </div>

    </el-timeline-item>
  </el-timeline>
</template>

<script>
export default {
  name: 'TimeLine',
  data() {
    return {
      drawer: false,
      activities: [{
        content: 'Log4j2 RCE 首次出现',
        timestamp: '2021-12-07',
        size: 'small',
        type: 'primary',
        icon: 'el-icon-more'
      },
      {
        content: '官方发布2.15.0-rc1版本以修复漏洞',
        timestamp: '2021-12-07',
        size: 'small',
        type: 'primary',
        icon: 'el-icon-more'
      },
      {
        content: 'Log4j2 RCE漏洞细节披露',
        timestamp: '2021-12-09',
        size: 'small',
        type: 'primary',
        icon: 'el-icon-more'
      },
      {
        content: '官方再次修复版本log4j-2.15.0-rc2',
        timestamp: '2021-12-10',
        size: 'small',
        type: 'primary',
        icon: 'el-icon-more'
      },
      {
        content: '发布安全通告，CVE编号为CVE-2021-44228',
        timestamp: '2021-12-10',
        size: 'large',
        type: 'primary',
        icon: 'el-icon-more'
      }]
    }
  }
}
</script>

<style scoped>

</style>

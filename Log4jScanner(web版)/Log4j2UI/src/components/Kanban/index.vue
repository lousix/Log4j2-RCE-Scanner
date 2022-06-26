<template>
  <div class="board-column">
    <div
      class="board-column-content"
      :list="list"
      v-bind="$attrs"
      :set-data="setData"
    >
      <div v-for="element in list" :key="element.id" class="board-item">
        <svg-icon :icon-class="element.icons" class="wrapper wrapper-money"/>
        <div class="card-panel-description">
          <div class="card-panel-text">{{ element.name }}</div>
          <count-to
            ref="example"
            :start-val="element.start"
            :end-val="element.end"
            :duration="2000"
            :decimals="0"
            :separator="','"
            :autoplay="true"
            class="card-panel-num"
          />
        </div>
      </div>
    </div>
    <!--/draggable-->
  </div>
</template>

<script>
import CountTo from 'vue-count-to'
export default {
  name: 'DragKanbanDemo',
  components: {
    CountTo
  },
  props: {
    headerText: {
      type: String,
      default: 'Header'
    },
    options: {
      type: Object,
      default() {
        return {}
      }
    },
    list: {
      type: Array,
      default() {
        return []
      }
    }
  },
  methods: {
    setData(dataTransfer) {
      // to avoid Firefox bug
      // Detail see : https://github.com/RubaXa/Sortable/issues/1012
      dataTransfer.setData('Text', '')
    }
  }
}
</script>
<style lang="scss" scoped>
.board-column {
  min-width: 300px;
  min-height: 100px;
  height: auto;
  overflow: hidden;
  background: #fff;
  border-radius: 3px;

  .board-column-header {
    height: 50px;
    line-height: 50px;
    overflow: hidden;
    padding: 0 20px;
    text-align: center;
    background: #333;
    color: #fff;
    border-radius: 3px 3px 0 0;
  }

  .board-column-content {
    height: auto;
    overflow: hidden;
    border: 10px solid transparent;
    min-height: 60px;
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    align-items: center;

    .board-item {
      cursor: pointer;
      width: 100%;
      height: 100px;
      margin: 25px 0;
      background-color: #fff;
      text-align: left;
      line-height: 54px;
      padding: 5px 10px;
      box-sizing: border-box;
      box-shadow: 0px 1px 3px 0 rgba(0, 0, 0, 0.2);

      font-size: 12px;
      position: relative;
      overflow: hidden;
      color: #666;
      border-color: rgba(0, 0, 0, .05);
      &:hover {
        .wrapper {
          color: #fff;
        }

        .wrapper-money{
          background: #f4516c;
        }
      }
    }

    .wrapper {
      float: left;
      margin: 10px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
      font-size: 70px;
    }
  }
}

.card-panel-description {
  float: right;
  font-weight: bold;
  margin: 20px;
  margin-left: 0px;

  .card-panel-text {
    line-height: 10px;
    color: rgba(0, 0, 0, 0.45);
    font-size: 18px;
    margin-bottom: 10px;
  }

  .card-panel-num {
    margin-top: -10px;
    line-height: 20px;
    font-size: 24px;
    margin-bottom: 10px;
  }
}

</style>


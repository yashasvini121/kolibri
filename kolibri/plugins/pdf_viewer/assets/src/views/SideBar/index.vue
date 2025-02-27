<template>

  <aside
    class="pdf-sidebar"
    :style="{
      background: $themeTokens.surface,
    }"
  >
    <nav :style="{ height: '100%' }">
      <KGrid gutter="0">
        <KGridItem
          v-for="tab in tabs"
          :key="tab.name"
          :ref="tab.name"
          :layout12="{ span: 4, alignment: 'center' }"
          :style="{
            background: selectedTab === tab.name ?
              $themeTokens.annotation :
              $themeTokens.transparent,
            cursor: 'pointer',
            borderRadius: '2px',
            opacity: tab.disabled ? 0.5 : 1,
            pointerEvents: tab.disabled ? 'none' : 'auto',
            height: '48px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }"
        >
          <div
            class="tab"
            :tabindex="tab.disabled ? -1 : 0"
            :aria-label="tab.name"
            role="button"
            @click="selectTab(tab.name)"
            @keydown.enter="selectTab(tab.name)"
            @keydown.space="selectTab(tab.name)"
          >
            <KIcon
              :icon="tab.icon"
              :style="{
                fill: selectedTab === tab.name ?
                  $themeTokens.textInverted :
                  $themeTokens.text,
                height: '24px',
                width: '24px',
              }"
            />
            <KTooltip
              :reference="tab.name"
              :refs="$refs"
            >
              {{ tab.label }}
            </KTooltip>
          </div>
        </KGridItem>
      </KGrid>
      <div class="sidebar-content">
        <template v-if="selectedTab === 'bookmarks'">
          <Bookmarks
            :outline="outline"
            :goToDestination="goToDestination"
            :focusDestPage="focusDestPage"
          />
        </template>
        <template v-if="selectedTab === 'preview'">
          <span> Preview </span>
        </template>
        <template v-if="selectedTab === 'annotations'">
          <span> Annotations </span>
        </template>
      </div>
    </nav>
  </aside>

</template>


<script>

  import Bookmarks from './Bookmarks';

  export default {
    name: 'SideBar',
    components: {
      Bookmarks,
    },
    props: {
      outline: {
        type: Array,
        required: true,
      },
      goToDestination: {
        type: Function,
        required: true,
      },
      focusDestPage: {
        type: Function,
        required: true,
      },
    },
    data() {
      return {
        selectedTab: 'bookmarks',
        tabs: [
          {
            name: 'bookmarks',
            label: 'Bookmarks',
            icon: 'list',
            disabled: false,
          },
          {
            name: 'preview',
            label: 'Preview',
            icon: 'channel',
            disabled: true,
          },
          {
            name: 'annotations',
            label: 'Annotations',
            icon: 'edit',
            disabled: true,
          },
        ],
      };
    },
    watch: {
      outline() {
        this.tabs[0].disabled = !this.outline || !this.outline.length;
        this.selectedTab = this.outline && this.outline.length ? 'bookmarks' : 'preview';
      },
    },
    methods: {
      selectTab(tabName) {
        this.selectedTab = tabName;
      },
    },
  };

</script>


<style scoped lang="scss">

  $sidebar-nav-height: 48px;

  .pdf-sidebar {
    height: 100%;
    box-shadow: inset -1px 2px 8px rgba(0, 0, 0, 0.16);
  }

  .tab:focus-visible {
    outline-width: 3px;
    outline-style: solid;
    outline-color: #8dc5b6;
    outline-offset: 4px;
  }

  .sidebar-content {
    height: calc(100% - #{$sidebar-nav-height});
    overflow-y: auto;
  }

</style>

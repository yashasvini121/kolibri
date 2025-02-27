<template>

  <div
    ref="header"
    class="header"
    :style="{
      backgroundColor: $themeTokens.surface,
      borderBottom: `1px solid ${$themeTokens.fineLine}`
    }"
  >
    <KGrid gutter="0">
      <KGridItem
        class="breadcrumbs"
        data-test="header-breadcrumbs"
        :layout4="{ span: 4 }"
        :layout8="{ span: 8 }"
        :layout12="{ span: 12 }"
      >
        <KBreadcrumbs
          v-if="breadcrumbs.length"
          :items="breadcrumbs"
          :ariaLabel="learnString('channelAndFoldersLabel')"
        />
      </KGridItem>
      <KGridItem
        :layout4="{ span: 4, alignment: 'auto' }"
        :layout8="{ span: 8, alignment: 'auto' }"
        :layout12="{ span: 12, alignment: 'auto' }"
      >
        <h1 class="title" data-test="header-title">
          <TextTruncator
            :text="title"
            :maxHeight="60"
          />
        </h1>
      </KGridItem>

      <KGridItem
        v-if="thumbnail"
        class="thumbnail"
        :layout4="{ span: 1 }"
        :layout8="{ span: 2 }"
        :layout12="{ span: 2 }"
      >
        <CardThumbnail
          class="thumbnail"
          :thumbnail="thumbnail"
          :isMobile="windowIsSmall"
          :showTooltip="false"
          kind="channel"
          :showContentIcon="false"
        />
      </KGridItem>

      <!-- tagline or description -->
      <KGridItem
        v-if="description"
        class="text"
        :layout4="{ span: thumbnail ? 3 : 4, alignment: 'auto' }"
        :layout8="{ span: thumbnail ? 6 : 8, alignment: 'auto' }"
        :layout12="{ span: thumbnail ? 10 : 12, alignment: 'auto' }"
      >
        <TextTruncator
          :text="description"
          :maxHeight="110"
        />
      </KGridItem>
    </KGrid>


  </div>

</template>


<script>

  import commonCoreStrings from 'kolibri.coreVue.mixins.commonCoreStrings';
  import KBreadcrumbs from 'kolibri-design-system/lib/KBreadcrumbs';
  import TextTruncator from 'kolibri.coreVue.components.TextTruncator';
  import responsiveWindowMixin from 'kolibri.coreVue.mixins.responsiveWindowMixin';
  import CardThumbnail from '../ContentCard/CardThumbnail';
  import commonLearnStrings from './../commonLearnStrings';

  export default {
    name: 'TopicsHeader',
    components: {
      CardThumbnail,
      KBreadcrumbs,
      TextTruncator,
    },
    mixins: [responsiveWindowMixin, commonCoreStrings, commonLearnStrings],
    props: {
      title: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        default: null,
      },
      thumbnail: {
        type: String,
        default: null,
      },
      breadcrumbs: {
        type: Array,
        required: true,
      },
    },
  };

</script>


<style lang="scss" scoped>

  @import '~kolibri-design-system/lib/styles/definitions';

  $header-height: 324px;
  $toolbar-height: 70px;

  .header {
    position: relative;
    top: $toolbar-height;
    width: 100%;
    height: $header-height;
    padding-top: 16px;
    padding-right: 32px;
    padding-bottom: 0;
    padding-left: 32px;
  }

  .title {
    margin: 8px 0 16px;
  }

</style>

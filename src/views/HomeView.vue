<template>
  <div class="h-96 flex justify-center items-center">
    <div class="w-full flex justify-center my-6">
      <MicButton :isActive="isOn" @click="test"/>
    </div>
  </div>
  <transition name="listening">
  <h1 v-if="isOn" class="text-6xl">Listening...</h1>
  </transition>
</template>

<script>
import MicButton from '@/components/MicButton.vue';

export default {
  name: 'HomeView',
  components:{
    MicButton
  },
  data(){
    return {
      isOn: false
    }
  },
  mounted() {
    window.ipcRenderer.receive('scriptClosed', (event, code) => {
      this.isOn = false;
    });
  },
  methods:{
    startListening(){
      window.ipcRenderer.send("testChannel",'start:script');
      this.isOn = true;
    },
    stopListening(){
      window.ipcRenderer.send("testChannel",'stop:script');
    },
    test(){
      if (!this.isOn){
        this.startListening();
      } else {
        this.stopListening();
      }
    }
  }
}
</script>

<style>
.listening-enter-active, .listening-leave-active {
  transition: opacity 0.5s;
}
.listening-enter, .listening-leave-to {
  opacity: 0;
}
</style>

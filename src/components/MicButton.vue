<template>
  <div class="flex justify-center items-center relative h-40 w-40 cursor-pointer">
    <!-- Halo rouge -->
    <div class="absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75" :class="{'animate-ping': isActive}"></div>
    <!-- Cercle -->
    <div class="relative inline-flex w-full h-40 rounded-full bg-red-500 justify-center items-center">
        <!-- Icône du microphone -->
        <span class="material-symbols-outlined text-9xl text-white">
        mic
        </span>
    </div>
    </div>
</template>

<script>
export default {
    props:{
        isActive:{
            type:Boolean,
            default:false
        }
    }
}
</script>

<style>

</style>
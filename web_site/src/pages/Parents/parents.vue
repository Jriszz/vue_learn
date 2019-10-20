<template>	
	<div>
		parents :{{info}}
		<Child	:title="msg"
		@sendMsg = "handlerMsg"/>
	</div>

</template>

<script>
	import Child from '@/pages/Parents/Child/Child';
	export default {
		name: "parents",
		components:{Child},
	data () {
		return {
			msg : "hello son",
			info : ""
		}

	},
	methods: {
		handlerMsg(info){
			this.info = info
		}
	}	

	}

</script>
<style scoped>
</style>
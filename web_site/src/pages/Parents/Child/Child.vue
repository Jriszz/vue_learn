<template>
	<div>
		Child:111
		receive from parent: {{ title }}
		<button @click="sendMsg">按钮</button>
	</div>
</template>

<script>
	export default {
		name: "Child",
		data () {
			return {

			}
		},
		props :{
			title: {
				type: String,
				default:""
			}
		},
		methods: {
			sendMsg(){
				this.$emit("sendMsg","this message from son")
			}
		}
	}
</script>
<style lang="scss" scoped>
	

</style>
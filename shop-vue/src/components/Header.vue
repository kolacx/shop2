<template>

<div class="bag">
	<p>{{headerText}}</p>
</div>

</template>
<script>

export default {
		name: "Header",
		data() {
			return {
				headerText: 'Header',
				menu: [],
			}
		},
		beforeCreate() {
			this.axios
			  .get('http://127.0.0.1:8000/api/v1/menu/')
			  .then(response => (this.menu = response.data.data));
		}
	}
</script>
<style >
</style>
<template>
	<div>
		<!-- <router-link to="/shop">Перейти к Foo</router-link> -->
		<p>{{ content }}</p>
		<p v-for="item in menu">{{ item }}</p>


		<!-- <app-h></app-h> -->
	</div>
</template>

<script>

import Header from './Header.vue'

	export default {
		name: "Home",
		components:{
			'app-h' : Header
		},
		data() {
			return {
				content: 'content! Home',
				menu: [],
			}
		},
		beforeCreate() {
			this.axios
			  .get('http://127.0.0.1:8000/api/v1/card/', {params: {cart_id: 3}})
			  .then(response => (this.menu = response.data.data));
		}
	}
</script>
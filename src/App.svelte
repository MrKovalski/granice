<script>
import Datatable from './Datatable.svelte';
</script>

<main>
	<div class="container">
		<header>
			<h1><span>OTVORENE GRANICE</span> | u doba korone</h1>
		</header>
		<div class="content">
			<Datatable />
		</div>
	</div>
</main>

<style>
.container{
	width: 60vw;
	height: 100vh;
	margin: 0 auto;
	color: rgb(201, 179, 179);
}
.content{
	border: 1px solid rgba(124, 111, 111, 0.39);
	padding: 1em;
	border-radius: 1em;
}
h1{
	text-align: center;
}
</style>
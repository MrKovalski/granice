<script>
import Datatable from './Datatable.svelte';
import Header from './Header.svelte';
import Buttons from './Buttons.svelte';
</script>

<main>
	<div class="container">
		<Buttons />
		<Header />
		<div class="content">
			<Datatable />
		</div>
	</div>
</main>

<style>
@media (max-width: 5199.98px){
	.container{
		width: 70vw;
		height: 100%;
		margin: 0 auto;
	}
}
@media (max-width: 575.98px){
	.container{
		width: 90vw;
		padding: 1em;
		height: 100%;
		margin: 0 auto;
	}
}
</style>
<script>
    import data from './static/data/zemlje.json'

import { Datatable, rows } from 'svelte-simple-datatables'

const settings = {
	sortable: true,
	pagination: true,
	rowPerPage: 50,
	columnFilter: true,
	css: true,
	labels: {
        search: 'Pretraži...',    // search input placeholer
        filter: 'Filter',       // filter inputs placeholder
        noRows: 'Nema polja',
        info: 'Prikazano od {start} do {end} od ukupno {rows} zemalja',
        previous: 'Prethodno',
        next: 'Sledeće',       
    }
}
</script>


<table>
    <thead>
        <th>DRŽAVA</th>
        <th>ULAZAK</th>
    </thead>
    <tbody>
        {#each data as d}
        <tr>
            <td>{d.zemlja}</td>
            <td class="ulazak-icons">{d.ulazak}</td>
        </tr>
    {/each}
    </tbody>
</table>

<style>
table{
    margin: 0 auto;
}
th{
    width:50%;
    }
td{
    text-align:center;
    padding:4px 0;
    }
.ulazak-icons{
    font-size: 2em;
}
</style>
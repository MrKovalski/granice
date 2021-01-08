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

<div id="tbl">
    <Datatable settings={settings} data={data}>
    <thead>
        <th data-key="zemlja">ZEMLJA</th>
        <th data-key="ulazak">STATUS</th>
    </thead>
    <tbody>
    {#each $rows as row}
        <tr>
            <td class="zemlja">{row.zemlja}</td>
            <td class="ulazak-icons">{row.ulazak}</td>
        </tr>
    {/each}
    </tbody>
</Datatable>    
</div>

<style>
#tbl{
    margin: 0 auto;
    height: 85vh;
}
td{
    text-align:center;
    padding:4px 0;
}
.ulazak-icons{
    font-size: 2em;
}
@media (max-width: 575.98px){
.ulazak-icons{
    font-size: 1.5em;
}
}
</style>
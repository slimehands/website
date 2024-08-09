<script>
	// @ts-ignore
	export let data;
	const { title, level, Content, slug} = data;
	console.log(data)
</script>
<link rel="stylesheet" href="/style.css"/>
<article>
	<h1>{title}</h1>
	<p>level: {level}</p>
	<Content />
	<a href={slug}>link</a>
</article>

<style>
	tr {
		border-right: medium black;
	}
</style>
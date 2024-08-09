<!-- src/routes/blog/+page.svelte -->
<script>
	export let data;
</script>

<h1>Blog</h1>

<ul>
	{#each data.posts as post}
		<li>
			<h2>
				<a href={post.slug}>
					here
				</a>
			</h2>
		</li>
	{/each}
</ul>
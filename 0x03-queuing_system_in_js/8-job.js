export default function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

	jobs.forEach((job) => {
		const aJob = queue.create('push_notification_code_3', job).save((err) => {
			if (!err) {
				console.log(`Notification job created: ${aJob.id}`);
			}
		});

		aJob.on('progress', (progress) => {
			console.log(`Notification job ${aJob.id} ${progress}% complete`);
		});

		aJob.on('complete', () => {
			console.log(`Notification job ${aJob.id} completed`);
		});

		aJob.on('failed', (err) => {
			console.log(`Notification job ${aJob.id} failed: ${err}`);
		});
	});
}

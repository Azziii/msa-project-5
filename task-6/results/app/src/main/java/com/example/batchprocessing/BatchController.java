package com.example.batchprocessing;

import org.springframework.batch.core.Job;
import org.springframework.batch.core.JobParametersBuilder;
import org.springframework.batch.core.launch.JobLauncher;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/batch")
public class BatchController {

    private final JobLauncher jobLauncher;
    private final Job importProductJob;

    public BatchController(
            JobLauncher jobLauncher,
            Job importProductJob) {

        this.jobLauncher = jobLauncher;
        this.importProductJob = importProductJob;
    }

    @PostMapping("/run")
    public String runJob() throws Exception {

        jobLauncher.run(
                importProductJob,
                new JobParametersBuilder()
                        .addLong(
                                "time",
                                System.currentTimeMillis())
                        .toJobParameters());

        return "Job started";
    }
}
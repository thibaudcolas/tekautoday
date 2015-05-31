'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var sass = require('gulp-sass');
var pleeease = require('gulp-pleeease');
var scsslint = require('gulp-scss-lint');

var reload = browserSync.reload;

var AUTOPREFIXER_BROWSERS = [
    'ie >= 10',
    'ie_mob >= 10',
    'ff >= 30',
    'chrome >= 34',
    'safari >= 7',
    'opera >= 23',
    'ios >= 7',
    'android >= 4.4',
    'bb >= 10'
];

gulp.task('build:css', function() {
    return gulp.src(['src/sass/*.scss'])
        .pipe(sass({
            errLogToConsole: true,
            precision: 10
        }))
        .pipe(pleeease({
            minifier: true,
            sourcemaps: false,
            mqpacker: true,
            filters: true,
            rem: true,
            pseudoElements: true,
            opacity: true,
            autoprefixer: {
                browsers: AUTOPREFIXER_BROWSERS
            }
        }))
        .pipe(gulp.dest('src/static/css'))
        .pipe(reload({stream: true}));
});

gulp.task('build', ['build:css']);

gulp.task('lint:css', function() {
    return gulp.src(['src/sass/*.scss'])
        .pipe(scsslint());
});

gulp.task('lint', ['lint:css']);

gulp.task('watch', ['build', 'lint'], function() {
    browserSync({
        proxy: 'http://localhost:5000/'
    });

    gulp.watch(['src/*.py', 'src/templates/*.html'], reload);
    gulp.watch(['src/sass/**/*.{scss,css}'], ['build:css', 'lint:css']);
});

gulp.task('default', ['watch']);

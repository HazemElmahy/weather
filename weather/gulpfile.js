const { gulp, src, dest, series, watch } = require('gulp');
const sass = require('gulp-sass');
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const terser = require('gulp-terser');


// SASS Task
function scssTask() {
    return src('./static/src/scss/main.scss', { sourcemaps: true })
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([cssnano()]))
    .pipe(dest('./static/build/css', { sourcemaps: '.'}))
}

// JavaScript Task
function jsTask() {
    return src('./static/src/js/*.js', {sourcemaps: true})
    .pipe(terser())
    .pipe(dest('./static/build/js', {sourcemaps: '.'}));
}

// Watch Task
function watchTask() {
    watch(['./static/src/scss/**/*.scss','./static/src/js/**/*.js'], 
     series(scssTask, jsTask));
}

// Default Gulp Task
exports.default = series(
    scssTask,
    jsTask,
    watchTask
)
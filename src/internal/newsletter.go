package internal

type Article struct {
	Date      string   `yaml:"date"`
	Title     string   `yaml:"title"`
	Author    string   `yaml:"author"`
	Thumbnail string   `yaml:"thumbnail"`
	Link      string   `yaml:"link"`
	Tags      []string `yaml:"tags"`
	Summary   string   `yaml:"summary"`
	Opinion   string   `yaml:"opinion"`
	TranslatedPath map[string]string `yaml:"translated_path"`
}

type Newsletter struct {
	Articles []Article `yaml:"articles"`
}
